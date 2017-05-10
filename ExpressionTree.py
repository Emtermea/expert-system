from srcs.Node import Node
from srcs.Expression import Expression
from srcs.OpAND import OpAND
from srcs.OpOR import OpOR
from srcs.OpXOR import OpXOR
from srcs.OpNOT import OpNOT
from srcs.Letter import Letter
from srcs.Implies import Implies
from srcs.OnlyIf import OnlyIf
from srcs.Rules import Rules
from srcs.toolsForTrees import *
# from srcs.resolv import *

# R0: C => E
# R1: A + B + C => D
# R2: A | B => C
# R3: A + !B => F
# R4: C | !G => H
# R5: V ^ W => X
# R6: A + B => Y + Z
# R7: C | D => X | V
# R8: E + F => !V

C = Letter("C")
A = Letter("A")
B = Letter("B")
E = Letter("E")
D = Letter("D")
F = Letter("F")
G = Letter("G")
H = Letter("H")
V = Letter("V")
W = Letter("W")
X = Letter("X")
Y = Letter("Y")
Z = Letter("Z")

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

# R2:
eqR2 = Implies()
oporR2 = OpOR()

nAR2 = Node(A)
nBR2 = Node(B)
nCR2 = Node(C)

nORR2 = Node(oporR2)

nORR2.left = nAR2
nORR2.right = nBR2

expLeftR2 = Expression(nORR2)
expRightR2 = Expression(nCR2)

rule2 = Rules(expLeftR2, eqR2, expRightR2)

# R3: A + !B => F
eqR3 = Implies()
opandR3 = OpAND()
opnotR3 = OpNOT()

nAR3 = Node(A)
nBR3 = Node(B)
nFR3 = Node(F)

nNOTR3 = Node(opnotR3)
nANDR3 = Node(opandR3)

nNOTR3.right = nBR3
nANDR3.left = nAR3
nANDR3.right = nNOTR3

expLeftR3 = Expression(nANDR3)
expRightR3 = Expression(nFR3)

rule3 = Rules(expLeftR3, eqR3, expRightR3)

# R4: C | !G => H
eqR4 = Implies()
oporR4 = OpOR()
opnotR4 = OpNOT()

nCR4 = Node(C)
nGR4 = Node(G)
nHR4 = Node(H)

nNOTR4 = Node(opnotR4)
nORR4 = Node(oporR4)

nNOTR4.right = nGR4
nORR4.left = nCR4
nORR4.right = nNOTR4

expLeftR4 = Expression(nORR4)
expRightR4 = Expression(nHR4)

rule4 = Rules(expLeftR4, eqR4, expRightR4)

# R5: V ^ W => X
eqR5 = Implies()
opxorR5 = OpXOR()

nVR5 = Node(V)
nWR5 = Node(W)
nXR5 = Node(X)

nXORR5 = Node(opxorR5)

nXORR5.left = nVR5
nXORR5.right = nWR5

expLeftR5 = Expression(nXORR5)
expRightR5 = Expression(nXR5)

rule5 = Rules(expLeftR5, eqR5, expRightR5)

# R6: A + B => Y + Z
eqR6 = Implies()
opand1R6 = OpAND()
opand2R6 = OpAND()

nAR6 = Node(A)
nBR6 = Node(B)
nYR6 = Node(Y)
nZR6 = Node(Z)

nAND1R6 = Node(opand1R6)
nAND2R6 = Node(opand2R6)

nAND1R6.left = nAR6
nAND1R6.right = nBR6

nAND2R6.left = nYR6
nAND2R6.right = nZR6

expLeftR6 = Expression(nAND1R6)
expRightR6 = Expression(nAND2R6)

rule6 = Rules(expLeftR6, eqR6, expRightR6)

# R7: C | D => X | V
eqR7 = Implies()
opor1R7 = OpOR()
opor2R7 = OpOR()

nCR7 = Node(C)
nDR7 = Node(D)
nXR7 = Node(X)
nVR7 = Node(V)

nOR1R7 = Node(opor1R7)
nOR2R7 = Node(opor2R7)

nOR1R7.left = nCR7
nOR1R7.right = nDR7

nOR2R7.left = nXR7
nOR2R7.right = nVR7

expLeftR7 = Expression(nOR1R7)
expRightR7 = Expression(nOR2R7)

rule7 = Rules(expLeftR7, eqR7, expRightR7)

# R8: E + F => !V
eqR8 = Implies()
opandR8 = OpAND()
opnotR8 = OpNOT()

nER8 = Node(E)
nFR8 = Node(F)
nVR8 = Node(V)

nANDR8 = Node(opandR8)
nNOTR8 = Node(opnotR8)

nANDR8.left = nER8
nANDR8.right = nFR8
nNOTR8.right = nVR8

expLeftR8 = Expression(nANDR8)
expRightR8 = Expression(nNOTR8)

rule8 = Rules(expLeftR8, eqR8, expRightR8)

# R9: A + B <=> C
eqR9 = OnlyIf()
opandR9 = OpAND()

nAR9 = Node(A)
nBR9 = Node(B)
nCR9 = Node(C)

nANDR9 = Node(opandR9)

nANDR9.left = nAR9
nANDR9.right = nBR9

expLeftR9 = Expression(nANDR9)
expRightR9 = Expression(nCR9)

rule9 = Rules(expLeftR9, eqR9, expRightR9)

# R10: A + B <=> !C
eqR10 = OnlyIf()
opandR10 = OpAND()
opnotR10 = OpNOT()

nAR10 = Node(A)
nBR10 = Node(B)
nCR10 = Node(C)

nANDR10 = Node(opandR10)
nNOTR10 = Node(opnotR10)

nANDR10.left = nAR10
nANDR10.right = nBR10
nNOTR10.right = nCR10

expLeftR10 = Expression(nANDR10)
expRightR10 = Expression(nNOTR10)

rule10 = Rules(expLeftR10, eqR10, expRightR10)

# parcourir rulesBase pour trouver une regle executable // comparer rule1.exp1 avec factsBase
rulesBase = [rule0, rule1, rule2, rule3, rule4, rule5, rule6, rule6, rule7, rule8, rule9, rule10]

# pour executer la regle :
# voir le papier
factsBase = [A, B, G]

for letter in factsBase:
	letter.setTrue()

printValue(expLeftR8.node)

abc = checkTypeNode(expLeftR8.node)
if abc == expLeftR8.node.value.typeOp:
	print ApplyRuleOnNode(expLeftR8.node)
	# print abc

# print checkTypeNode(expLeftR1.node.value)
# print "retour de checktype :"
# checkTypeNode(expLeftR8.node)
# printValue(expLeftR1.node)

# resolv(factsBase, rulesBase, G)
