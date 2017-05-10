from Letter import Letter
from Operator import Operator

def printValue(node):
	if node.left:
		printValue(node.left)
	if node.right:
		printValue(node.right)
	try:
		node.value.typeOp
		print node.value.typeOp
	except:
		print node.value.letter
		print node.value.value
