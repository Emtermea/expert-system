from srcs.Node import Node
from srcs.Expression import Expression
from srcs.OpAND import OpAND
from srcs.Letter import Letter
from srcs.Implies import Implies
from srcs.Rules import Rules

# A = Letter("A")
# B = Letter("B")
# C = Letter("C")

# A.setTrue()
# B.setTrue()

# And = OpAND()
# Op = Implies()

# exp1 = [A, And, B, Or, exp3]]
# exp2 = [C]

# rules = Rules(exp1, Op, exp2)

# print And.apply(A, B)

# La construction des arbres binaire (des expressions) sera fait dans le parser
# voici un example
# nOR = Node("OR")
# nAND1 = Node("AND")
# nAND2 = Node("AND")
# nA = Node("A")
# nB = Node("B")
# nC = Node("C")
# nD = Node("D")

# nOR.left = nB
# nOR.right = nC

# nAND2.left = nA
# nAND2.right = nOR

# nAND1.left = nAND2
# nAND1.right = nD
# fin de l'example de la construction d'un arbre

# exp1 = Expression(nAND1)



# R0: C => E
# R1: A + B + C => D
C = Letter("C")
A = Letter("A")
B = Letter("B")
E = Letter("E")
D = Letter("D")

# R0:
eqR0 = Implies()

nCR0 = Node(C)
nER0 = Node(E)

expLeftR0 = Expression(nCR0)
expRightR0 = Expression(nER0)

rule0 = Rules(expLeftR0, eqR0, expRightR0)

# R1:
eqR1 = Implies()
opand1R1 = OpAND()
opand2R1 = OpAND()

nAR1 = Node(A)
nBR1 = Node(B)
nCR1 = Node(C)
nDR1 = Node(D)

nAND1R1 = Node(opand1R1)
nAND2R1 = Node(opand2R1)

nAND1R1.left = nAR1
nAND1R1.right = nBR1
nAND2R1.left = nAND1R1
nAND2R1.right = nCR1

expLeftR1 = Expression(nAND2R1)
expRightR1 = Expression(nDR1)

rule1 = Rules(expLeftR1, eqR1, expRightR1)


# parcourir rulesBase pour trouver une regle executable // comparer rule1.exp1 avec factsBase
rulesBase = [rule0, rule1]

# pour executer la regle :
# voir le papier
factsBase = [A, B, C]


def printValue(node):
    if (node.left):
        printValue(node.left)
    if (node.right):
        printValue(node.right)

    # if typeof node == Letter:
        # print node.value.value
    # else:
        # print node.value.typeOp

printValue(nAND2R1)
          