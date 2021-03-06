from Operator import Operator

class OpOR(Operator):
    """
        Represent le symbole "|"
    """
    def __init__(self):
        Operator.__init__(self, "OR")
    def apply(self, letterLeft, letterRight):
        return letterLeft.value or letterRight.value
