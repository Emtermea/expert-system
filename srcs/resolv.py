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

def applyRule(RelevantRule, factsBase): #appliquer la regle applicable
	# if RelevantRule.rightExp.node.value.letter:
	# 	if RelevantRule.rightExp.node.value.letter in factsBase:
	# 		pass
	# if RelevantRule.leftExp.node.value.typeOp and RelevantRule.rightExp.node.value.letter:
	# 	newValue = RelevantRule.leftExp.node.value.apply(RelevantRule.leftExp.node.left, RelevantRule.leftExp.node.right)
	# 	RelevantRule.rightExp.node.value.value = newValue.value
	# 	factsBase.append(RelevantRule.rightExp.node.value)
	if RelevantRule.leftExp.node.value.typeOp and RelevantRule.rightExp.node.value.typeOp:
		newValueL = RelevantRule.leftExp.node.value.apply(RelevantRule.leftExp.node.left, RelevantRule.leftExp.node.right)
		newValueR = RelevantRule.rightExp.node.value.apply(RelevantRule.rightExp.node.left, RelevantRule.rightExp.node.right)
		if newValueL != newValueR:
			pass
	elif RelevantRule.leftExp.node.value.typeOp and RelevantRule.rightExp.node.value.letter:
		newValue = RelevantRule.leftExp.node.value.apply(RelevantRule.leftExp.node.left, RelevantRule.leftExp.node.right)
		RelevantRule.rightExp.node.value = newValue
		factsBase.append(RelevantRule.rightExp.node.value)
	elif RelevantRule.leftExp.node.value.letter and RelevantRule.rightExp.node.value.letter:
		RelevantRule.rightExp.node.value.value = RelevantRule.leftExp.node.value.value
		factsBase.append(RelevantRule.rightExp.node.value)
	elif RelevantRule.leftExp.node.value.letter and RelevantRule.rightExp.node.value.typeOp:
		newValue = RelevantRule.rightExp.node.value.apply(RelevantRule.rightExp.node.left, RelevantRule.rightExp.node.right)
		RelevantRule.rightExp.node.value.value = newValue.value
		factsBase.append(RelevantRule.rightExp.node.value)
	return factsBase

def checkRelevantRule(rule, factsBase): #check si la regle est applicable
	lettersInRule = []
	getLetterNode(rule.leftExp.node, lettersInRule)
	for letter in lettersInRule:
		i = 0
		while i < len(factsBase):
			if letter != factsBase[i].letter:
				i += 1
			if lettersInRule.index(letter) == len(lettersInRule) - 1 and letter != factsBase[i].letter:
				return 0
			else:
				break
	return 1

def findRelevantRule(rulesBase, factsBase): # trouver la premier regle applicable
	for rule in rulesBase:
		if checkRelevantRule(rule, factsBase):
			return rule
	return 0

def resolv(factsBase, rulesBase, letter): # fonction de resolution
	i = 0
	while letter not in factsBase:
		while rulesBase:
			print "rule n : ", i
			RelevantRule = findRelevantRule(rulesBase, factsBase)
			printRule(RelevantRule)
			if RelevantRule:
				applyRule(RelevantRule, factsBase)
				i += 1
				rulesBase.remove(RelevantRule)
	for fact in factsBase:
		print fact.letter
		print fact.value


# while (letter not in factsBase) and RelevantRule:
	# apply le retour de RelevantRule
	# resolvExp
	# push le resultat de apply dans factsBase
	# desactivation de la regle:
	# rulesBase.remove(RelevantRule)
