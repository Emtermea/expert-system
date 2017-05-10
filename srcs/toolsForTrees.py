def printValue(node):
    if (node.left):
        printValue(node.left)
    if (node.right):
        printValue(node.right)

    # if typeof node == Letter:
        # print node.value.value
    # else:
        # print node.value.typeOp
