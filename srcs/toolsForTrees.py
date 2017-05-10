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

def checkTypeNode(node):
	if node.left:
		checkTypeNode(node.left)
	if node.right:
		checkTypeNode(node.right)
	try:
		return node.value.typeOp
	except:
		if not node.value.letter:
			checkTypeNode(node)
		else:
			return node.value.letter

# def ApplyRuleOnNode(node):
# 	if node.left:
# 		ApplyRuleOnNode(node.left)
# 	if node.right:
# 		ApplyRuleOnNode(node.right)
# 	try:
# 		return node.value.typeOp.apply(node.left, node.right)
# 	except:
# 		pass
