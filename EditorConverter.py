# Test version!!! Can destroy game save

from decoders import k4decoder, k4encoder


class LevelEditor:

    def __init__(self, level: str):
        editorstring = k4decoder(level)

        self.leveleditorsettings, *self.blockstring = editorstring.split(";")[:-1]

        self.blocks = []

        for block in self.blockstring:
            val = block.split(",")

            blockdata = {val[i]: val[i + 1] for i in range(0, len(val), 2)}

            if "57" in blockdata.keys():
                blockdata["57"] = blockdata["57"].split(".")

            self.blocks.append(blockdata)

            # translator(self.blocks)


    def damp(self):
        # ditranslator(self.blocks)

        blockstring = ";"

        for block in self.blocks:
            if "57" in block:
                block["57"] = ".".join(block["57"])

            for n, i in enumerate(block.items()):
                if n == 0:
                    blockstring += f"{i[0]},{i[1]}"
                else:
                    blockstring += f",{i[0]},{i[1]}"
            blockstring += ";"
        return k4encoder(self.leveleditorsettings + blockstring)


def translator(a):
    # import translate dict
    return a


def ditranslator(a):
    # import translate dict
    return a
