from Operator import Operator

class OpAND(Operator):
    """
        Represent le symbole "+"
    """
    def __init__(self):
        Operator.__init__(self, "AND")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value and letterRight.value
