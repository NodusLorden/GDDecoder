# string -> dict
def strtodict(sp: str, i: int = 3) -> (dict, int):

    """
    Convert xml string to dict
    :param sp: xml string (can use string after addlinebreak)
    :param i: start point of parsing
    :return: dict and end point
    Point i use in recursion, it can be omitted
    """
    if type(sp) == list:
        pass
    elif sp.count("\n") < 2:
        sp = addlinebreak(sp).split("\n")

    ln = len(sp)
    d = dict()

    while i + 1 < ln:

        val = sp[i + 1][:3]
        key = sp[i][3: -4]

        if val == "<k>":
            i += 1

        elif val == "<d>":
            i += 1
            d[key], i = strtodict(sp, i=i)

        elif val == "<t ":
            d[key] = True
            i += 1
        elif val == "<f ":
            d[key] = False
            i += 1
        elif val == "<d ":
            d[key] = dict()
            i += 1
        elif val == "<i>":
            d[key] = int(sp[i + 1][3: -4])
            i += 1
        elif val == "<r>":
            d[key] = float(sp[i + 1][3: -4])
            i += 1
        elif val == "<s>":
            d[key] = sp[i + 1][3: -4]
            i += 1

        elif val == "</d":
            i += 1
            return d, i
        else:
            print(val, "не обработано")


# string -> list of lines
def strtolist(st: str) -> list:
    """
    It is not advised to use this function!
    For list of strings use: addlinebreak(plist).split("\n")
    Works 7 times faster

    Converts an xml game string to a list of strings
    :param st: xml string
    :return: list of strings
    """
    ln = len(st)
    i = 0
    ns = []

    # Flags
    pt1 = 0

    while i < ln:
        if st[i] == "<":
            p1 = i

            while st[i] != ">":
                i += 1

            p2 = i
            part = st[p1 + 1: p2].split(" ")[0].lower()
            adv = st[p2 - 1]

            if part == "?xml":
                ns.append(st[p1: p2 + 1])

            elif part == "t" and adv == "/":
                ns.append(st[p1: p2 + 1])

            elif part == "f" and adv == "/":
                ns.append(st[p1: p2 + 1])

            elif part == "d" and adv == "/":
                ns.append(st[p1: p2 + 1])

            elif part == "d":
                ns.append(st[p1: p2 + 1])
            elif part == "/d":
                ns.append(st[p1: p2 + 1])

            elif part in ["k", "i", "s", "r"]:
                pt1 = p1
            elif part in ["/k", "/i", "/s", "/r"]:
                pt2 = p2
                ns.append(st[pt1: pt2 + 1])

            elif part == "plist":
                ns.append(st[p1: p2 + 1])
            elif part == "/plist":
                ns.append(st[p1: p2 + 1])

            elif part == "dict":
                ns.append(st[p1: p2 + 1])
            elif part == "/dict":
                ns.append(st[p1: p2 + 1])

        i += 1

    return ns


# string -> string with line break
def addlinebreak(st: str) -> str:
    """
    Adds line break to xml string
    :param st: xml string
    :return: string
    """
    ns = st.replace("</k>", "</k>\n").replace("</i>", "</i>\n").replace("</r>", "</r>\n").replace("</s>", "</s>\n").\
        replace("</d>", "</d>\n").replace("<d>", "<d>\n").replace("<d />", "<d />\n").replace("<t />", "<t />\n").\
        replace("<f />", "<f />\n").replace("<dict>", "<dict>\n").replace("</dict>", "</dict>\n").\
        replace("gjver=\"2.0\">", "gjver=\"2.0\">\n").replace("?>", "?>\n")

    return ns


# string -> plist string
def strtoplist(st: str) -> str:
    """
    Adds tabs and line breaks so that it can be opened and viewed in the plist editor
    :param st: xml string
    :return: xml string with tabs and line breaks
    """
    t = 0
    ln = len(st)
    i = 0
    ns = ""

    # Flags
    pt1 = 0

    while i < ln:
        if st[i] == "<":
            p1 = i

            while st[i] != ">":
                i += 1

            p2 = i
            part = st[p1 + 1: p2].split(" ")[0].lower()
            adv = st[p2 - 1]

            if part == "?xml":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "t" and adv == "/":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "f" and adv == "/":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "d" and adv == "/":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "plist":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"
                t += 1
            elif part == "/plist":
                t -= 1
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "dict":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"
                t += 1
            elif part == "/dict":
                t -= 1
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part == "d":
                ns += t * "\t" + st[p1: p2 + 1] + "\n"
                t += 1
            elif part == "/d":
                t -= 1
                ns += t * "\t" + st[p1: p2 + 1] + "\n"

            elif part in ["k", "i", "s", "r"]:
                pt1 = p1
            elif part in ["/k", "/i", "/s", "/r"]:
                pt2 = p2
                ns += t * "\t" + st[pt1: pt2 + 1] + "\n"

        i += 1

    return ns


# dict -> string
def dicttostr(di: dict) -> str:
    """
    Converts a dictionary to a string for packing and saving
    :param di: dict from xml
    :return: xml string without tabs and line breaks
    """
    s = ""
    for i in di.keys():
        if type(di[i]) == dict:
            if not di[i]:
                s += f"<k>{i}</k><d />"
            else:
                s += f"<k>{i}</k><d>{dicttostr(di[i])}</d>"
        elif type(di[i]) == str:
            s += f"<k>{i}</k><s>{di[i]}</s>"
        elif type(di[i]) == int:
            s += f"<k>{i}</k><i>{di[i]}</i>"
        elif type(di[i]) == float:
            if di[i].is_integer():
                di[i] = int(di[i])
            s += f"<k>{i}</k><r>{di[i]}</r>"
        elif type(di[i]) == bool:
            if di[i]:
                s += f"<k>{i}</k><t />"
            # else:
                # s += f"<k>{i}</k></ f>"

    return s
