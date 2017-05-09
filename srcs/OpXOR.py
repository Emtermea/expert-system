from Operator import Operator

class OpXOR(Operator):
    """
        Represent le symbole "^"
    """
    def __init__(self):
        Operator.__init__(self, "XOR")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value != letterRight.value
