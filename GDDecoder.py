import os
import getpass
from decoders import *
from converters import *
from json import dump, load


class GDLevels:

    def __init__(self, Filepath: str = None):
        if not Filepath:
            if os.path.isfile(f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\GeometryDash\\CCLocalLevels.dat"):
                self.FILEPATH = f"C:\\Users\\{getpass.getuser()}\\AppData\\Local\\GeometryDash\\CCLocalLevels.dat"
            else:
                raise FileNotFoundError(f"Файл C:\\Users\\{getpass.getuser()}\\AppData\\Local\\GeometryDash\\"
                                        f"CCLocalLevels.dat не найден. Если пусть к файлу не стандартный, "
                                        f"укажиет его как аргумент.")
        elif os.path.isfile(Filepath):
            self.FILEPATH = Filepath
        else:
            raise FileNotFoundError(f"По указанному пути {Filepath} файл не найден")

        with open(self.FILEPATH, mode="rb") as file:
            self.bfile = file.read()

        self.savepath = self.FILEPATH

        self.plist = str()
        self.filedict = dict()
        self.levels = dict()
        self.rude = dict()
        self.convertkey = False

    def load(self):
        self.plist = fromgzip(frombase64(xor(self.bfile)))
        self.filedict = strtodict(self.plist)[0]
        self.levels = self.filedict["LLM_01"]
        self.rude["LLM_02"] = self.filedict.pop("LLM_02")
        self.rude["_isArr"] = self.levels.pop("_isArr")
        return self

    def save(self):
        self.plist = f"<?xml version=\"1.0\"?><plist version=\"1.0\" gjver=\"2.0\"><dict><k>LLM_01</k>" \
                          f"<d><k>_isArr</k><{'t /' if self.rude['_isArr'] else 'f /'}>{dicttostr(self.levels)}</d>" \
                          f"<k>LLM_02</k><i>{self.rude['LLM_02']}</i></dict></plist>"
        self.bfile = xor(tobase64(togzip(self.plist)))
        with open(self.savepath, "wb") as f:
            f.write(self.bfile)
        return True

    def createloadpoint(self, path: str = "point.json"):
        if not (self.levels and self.rude and self.convertkey):
            self.load()
        with open(path, "w") as f:
            dump([self.FILEPATH, self.savepath, self.levels, self.rude, self.convertkey], f)
        return self

    def fastload(self, path: str = "point.json"):
        with open(path) as f:
            self.FILEPATH, self.savepath, self.levels, self.rude, self.convertkey = load(f)
        return self
