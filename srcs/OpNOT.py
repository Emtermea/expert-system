class OpNOT(Operator):
    def __init__(self):
        Operator.__init__(self, "NOT")
    def apply(self, letterLeft, letterRight):
        return not letterRight.value
