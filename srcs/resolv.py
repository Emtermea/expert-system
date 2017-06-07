import sys
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

def applyOp(nodeLeft, nodeRight, factsBase, b): # applique la fonction apply de l'operateur si a droite c'est une letter inconnue
	newValue = nodeLeft.value.apply(nodeLeft.left, nodeLeft.right)
	if b:
		nodeRight.value.value = newValue.value
		factsBase.append(nodeRight.value)
		return newValue.value
	else:
		return newValue

def applyRule(RelevantRule, factsBase): #appliquer la regle applicable
	if isinstance(RelevantRule.leftExp.node.value, Operator): # si a gauche il y a une op
		if isinstance(RelevantRule.rightExp.node.value, Letter): # si a droite c'est une letter
			if (RelevantRule.rightExp.node.value not in factsBase): # si la letter n'est pas connue
				applyOp(RelevantRule.leftExp.node, RelevantRule.rightExp.node, factsBase, 1)
			else: # si la letter est connue
				# comparer le resultat de apply avec la valeur de la letter connue
				print ('\x1b[0;37;45m' + "letter right in factsBase" + '\x1b[0m')
				if applyOp(RelevantRule.leftExp.node, RelevantRule.rightExp.node, factsBase, 0) == RelevantRule.rightExp.node.value.value:
					print ('\x1b[1;31;40m' + "everything is alright" + '\x1b[0m')
					pass
				else:
					print ('\x1b[1;31;40m' + 'conflict' + '\x1b[0m')
		else: # si a droite il y a une op a faire
			print ('\x1b[0;30;45m' + "RelevantRule.rightExp.node.value is a typeOp, need to call again function 1" + '\x1b[0m')
			RelevantRule.rightExp.node.value = applyOp(RelevantRule.rightExp.node, RelevantRule.rightExp.node, factsBase, 0)
			RelevantRule.leftExp.node.value = applyOp(RelevantRule.leftExp.node, RelevantRule.leftExp.node, factsBase, 0)
			if (RelevantRule.rightExp.node.value == RelevantRule.leftExp.node.value) and (il y a une letter sur au moins un des deux cotés):
				# append la letter et sa valuer dans factsBase
				print ('\x1b[1;32;40m' + "everything is alright 2 " + '\x1b[0m')
			else:
				# if il y a encore un Op qqpart:
					# executer l Op -> recursivité
				print ('\x1b[1;31;40m' + 'conflict 2' + '\x1b[0m')
	else: # si a gauche c'est une letter
		if isinstance(RelevantRule.rightExp.node.value, Letter): # si a droite c'est une letter aussi
			if (RelevantRule.rightExp.node.value in factsBase):
				# comparer la valeur de left avec la valeur de la letter connue
				if RelevantRule.rightExp.node.value.value == RelevantRule.leftExp.node.value.value:
					pass
				else:
					RelevantRule.rightExp.node.value.value == "undetermined"
			else: # si la letter de droite n'est pas connue
				# la valeur de right est egale a celle de gauche
				print "la valeur inconnue prend la valeur de la connue"
				RelevantRule.rightExp.node.value.value = RelevantRule.leftExp.node.value.value
				factsBase.append(RelevantRule.rightExp.node.value)
		else:
			#  recursivité
			print ('\x1b[0;30;45m' + "RelevantRule.rightExp.node.value is a typeOp, need to call again function 2" + '\x1b[0m')
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
		while rulesBase and (i < len(rulesBase)):
			print "i = ", i
			print "len de rulesBase : ", len(rulesBase)
			if checkRelevantRule(rulesBase[i], factsBase):
				print ('\x1b[1;32;40m' + "RelevantRule == 1" + '\x1b[0m')
				applyRule(rulesBase[i], factsBase)
			else:
				# condition de sortie si RelevantRule == 0
				print ('\x1b[1;31;40m' + "RelevantRule == 0" + '\x1b[0m')
				i += 1
				continue
			rulesBase.remove(rulesBase[i])
		sys.exit(0) # pour eviter la boucle infinie pendant les tests
	if letter in factsBase:
		print letter, " is ", letter.value

# while (letter not in factsBase) and RelevantRule:
	# apply le retour de RelevantRule
	# resolvExp
	# push le resultat de apply dans factsBase
	# desactivation de la regle:
	# rulesBase.remove(RelevantRule)
