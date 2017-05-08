class OpXOR(Operator):
    def __init__(self):
        Operator.__init__(self, "XOR")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value != letterRight.value
