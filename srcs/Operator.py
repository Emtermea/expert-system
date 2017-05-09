class Operator:
    """
        Une class generique qui represent une operation tel que l'operateur AND ou OR
        Il a un type parmit: AND, OR, XOR, NOT, IMPLIES ou ONLYIF
        Chaque Operator a une fonction "apply" qui gerera ses propres regles de logique 
    """
    def __init__(self, typeOp):
        self.typeOp = typeOp

   # @abstractmethod (peut etre plus tard pour faire plus propre)
    def apply(self, letterLeft, letterRight):
        pass
