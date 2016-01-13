# -*- coding: utf-8 -*-
from enum import Enum

class Lexem():

    class Mult(Enum):   # Число

        sing = "sing"   # Единственное
        plur = "plur"   # Множественное

    class Case (Enum):

        nomn = "nomn"   # Именительный
        gent = "gent"   # Родительный
        datv = "datv"   # Дательный
        accs = "accs"   # Винительный
        ablt = "ablt"   # Творительный
        loct = "loct"   # Предложный