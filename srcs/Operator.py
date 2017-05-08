class Operator:
    def __init__(self, typeOp):
        self.typeOp = typeOp

   # @abstractmethod (peut etre plus tard pour faire plus propre)
    def apply(self, letterLeft, letterRight):
        pass
