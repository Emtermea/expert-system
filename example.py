from enum import Enum

class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.value = 0

    # Apeller au moment du parser, potentiellement au moment ou on push dans factsBase
    def setTrue(self):
        self.value = 1


class Logical(Enum):
    UNKNOW = 0
    AND = 1
    OR = 2
    XOR = 3
    NOT = 4

class Operator:
    def __init__(self, logical):
        self.logical = self._getType(logical)

    def _getType(str):
        if (str == "+"):
            return Logical.AND
        elif (str == "!"):
            return Logical.NOT
        elif (str == "|"):
            return Logical.OR
        elif (str == "^"):
            return Logical.XOR
        else
            return Logical.UNKNOW

class Expression:
    def __init__(self):
        self.exp = []


class Rules:
    def __init__(self, leftExp, equal, rightExp):
        self.leftExp = leftExp
        self.equal = equal
        self.rightExp = rightExp


class Equal:
    def __init__(self):
        pass


# Tableau de Regles => table de Rules
# A la fin du lexser/parser d'une ligne, nouvelle instance de Rules
rulesBase = []

# Tableau de fait => table de Letter
# Quand la ligne commence par un '=', push les Lettre dans ce tableau
factsBase = []
