class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.value = False

    # Apeller au moment du parser, potentiellement au moment ou on push dans factsBase
    def setTrue(self):
        self.value = True


class Operator:
    def __init__(self, typeOp):
        self.typeOp = typeOp

   # @abstractmethod (peut etre plus tard pour faire plus propre)
    def apply(self, letterLeft, letterRight):
        pass

class OpAND(Operator):
    def __init__(self):
        Operator.__init__(self, "AND")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value and letterRight.value


class OpOR(Operator):
    def __init__(self):
        Operator.__init__(self, "OR")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value or letterRight.value

class OpXOR(Operator):
    def __init__(self):
        Operator.__init__(self, "XOR")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value != letterRight.value

class OpNOT(Operator):
    def __init__(self):
        Operator.__init__(self, "NOT")
    def apply(self, letterLeft, letterRight):
        return not letterRight.value


# Une expression est un arbre binaire
class Expression:
    def __init__(self, node):
        self.node = node


class Rules:
    def __init__(self, leftExp, equal, rightExp):
        self.leftExp = leftExp
        self.equal = equal
        self.rightExp = rightExp


class Equal(Operator):
    def __init__(self, typeOp):
        Operator.__init__(self, typeOp)
        

class Implies(Equal):
    def __init__(self):
        Equal.__init__(self, "IMPLIES")

    def apply(self, letterLeft, letterRight):
        if (letterLeft.value == True and letterRight.value == False):
            return False
        else:
            return True

class OnlyIf(Equal):
    def __init__(self):
        Equal.__init__(self, "ONLYIF")

    def apply(self, letterLeft, letterRight):
        return letterLeft.value == letterRight.value


# Tableau de Regles => table de Rules
# A la fin du lexser/parser d'une ligne, nouvelle instance de Rules
rulesBase = []

# Tableau de fait => table de Letter
# Quand la ligne commence par un '=', push les Lettre dans ce tableau
factsBase = []


A = Letter("A")
B = Letter("B")
C = Letter("C")

A.setTrue()
B.setTrue()

And = OpAND()
Op = Implies()

# exp1 = [A, And, B, Or, exp3]]
# exp2 = [C]

# rules = Rules(exp1, Op, exp2)

print And.apply(A, B)



class Node:
    def __init__(self, val):
        self.l = None
        self.r = None
        self.v = val

# La construction des arbres binaire (des expressions) sera fait dans le parser
# voici un example
nOR = Node("OR")
nAND1 = Node("AND")
nAND2 = Node("AND")
nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")

nOR.l = nB
nOR.r = nC

nAND2.l = nA
nAND2.r = nOR

nAND1.l = nAND2
nAND1.r = nD
# fin de l'example de la construction d'un arbre

exp1 = Expression(nAND1)
