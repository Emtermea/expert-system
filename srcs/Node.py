class Node:
    """
        Ceci est un noeud pour definir un arbre binaire
        Il contient un fils gauche et un fils droit

        Un fils peut etre un autre Node, ou un element final tel qu'un Letter
        Un Node sans enfants s'appel une "feuille"
    """
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value
