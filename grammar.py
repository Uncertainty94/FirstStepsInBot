from enum import Enum

class Grammar():
    class Mult(Enum):
        sing = "sing"
        plur = "plur"
    class Case (Enum):
        nomn = "nomn"
        gent = "gent"
        datv = "datv"
        accs = "accs"
        ablt = "ablt"
        loct = "loct"