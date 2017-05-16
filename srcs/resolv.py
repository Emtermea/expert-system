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

def applyRule(rule, ValueInNode): #appliquer la regle designee comme applicable
	pass

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
	RelevantRule = findRelevantRule(rulesBase, factsBase)
	return RelevantRule
	# while (letter not in factsBase) and RelevantRule:
		# apply le retour de RelevantRule
		# push le resultat de apply dans factsBase
		# desactivation de la regle:
		# rulesBase.remove(RelevantRule)
