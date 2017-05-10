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

def applyRule(rule):
	if checkTypeNode(rule.leftExp.node) == node.value.typeOp:
		A = node.value.typeOp.apply(node.letterLeft, node.letterRight)
	# if checkTypeNode(rule.rightExp.node) == node.value.typeOp:
		# B = node.value.typeOp.apply(node.letterLeft, node.letterRight)
	# rule.equal

	# rule.rightExp.node.value.value = le resultat de equal

# trouver une autre façon / iteration impossoble comme ca
def checkRelevantRule(rule, factsBase):
	lettersInRule = []
	for elem in rule.leftExp.node:
		if checkTypeNode(rule.leftExp.node) == node.value.letter:
			lettersInRule.append(rule.leftExp.node)
	for letter1 in lettersInRule:
    	for letter2 in factsBase:
        	if letter1 != letter2:
             	return 0
	return 1

def findRelevantRule(rulesBase, factsBase):
	for rule in rulesBase:
		if checkRelevantRule(rule, factsBase):
			return rule
	return 0

def resolv(factsBase, rulesBase, letter):
	RelevantRule = findRelevantRule(rulesBase, factsBase)
	while (letter not in factsBase) and RelevantRule:
		# apply le retour de RelevantRule
		# push le resultat de la regle dans factsBase

		# desactivation de la regle
		# rulesBase.remove(RelevantRule)
