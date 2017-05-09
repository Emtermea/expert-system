from srcs.Node import Node
from srcs.Expression import Expression
from srcs.OpAND import OpAND
from srcs.Letter import Letter
from srcs.Implies import Implies

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

# La construction des arbres binaire (des expressions) sera fait dans le parser
# voici un example
nOR = Node("OR")
nAND1 = Node("AND")
nAND2 = Node("AND")
nA = Node("A")
nB = Node("B")
nC = Node("C")
nD = Node("D")

nOR.left = nB
nOR.right = nC

nAND2.left = nA
nAND2.right = nOR

nAND1.left = nAND2
nAND1.right = nD
# fin de l'example de la construction d'un arbre

exp1 = Expression(nAND1)
