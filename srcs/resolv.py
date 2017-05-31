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
	if isinstance(RelevantRule.leftExp.node.value, Operator): # si a gauche il y a une op
		if isinstance(RelevantRule.rightExp.node.value, Letter): # si a droite c'est une letter
			if (RelevantRule.rightExp.node.value.letter not in factsBase): # si la letter n'est pas connue
				print "unknow letter right -> not in factsBase ==> need to apply typeOp"
				newValue = RelevantRule.leftExp.node.value.apply(RelevantRule.leftExp.node.left, RelevantRule.leftExp.node.right)
				RelevantRule.rightExp.node.value = newValue
				factsBase.append(RelevantRule.rightExp.node.value)
			else: # si la letter est connue
				# comparer le resultat de apply avec la valeur de la letter connue
				print "letter right in factsBase"
		else: # si a droite il y a une op a faire
			print "RelevantRule.rightExp.node.value is TYPEOP, need to call again function"
	else: # si a gauche c'est une letter
		if isinstance(RelevantRule.rightExp.node.value, Letter):
			if (RelevantRule.rightExp.node.value.letter in factsBase):
				# comparer la valeur de left avec la valeur de la letter connue
				print "letter right in factsBase"
			else:
				# la valeur de right est egale a celle de gauche
				print "la valeur inconnue prend la valeur de la connue"
		else:
			print "RelevantRule.rightExp.node.value is a typeOp, need to call again function"
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
# attention if ca retourne 0
#
def resolv(factsBase, rulesBase, letter): # fonction de resolution
	while letter not in factsBase:
		while rulesBase:
			RelevantRule = findRelevantRule(rulesBase, factsBase)
			print "retour de find rule", RelevantRule
			if RelevantRule:
				applyRule(RelevantRule, factsBase)
				rulesBase.remove(RelevantRule)
				print "on passe par la aussi"
			# else:
				# faire un econdition de sortie si RelevantRule == 0
	# for fact in factsBase:
	# 	print fact.letter
	# 	print fact.value


# while (letter not in factsBase) and RelevantRule:
	# apply le retour de RelevantRule
	# resolvExp
	# push le resultat de apply dans factsBase
	# desactivation de la regle:
	# rulesBase.remove(RelevantRule)
