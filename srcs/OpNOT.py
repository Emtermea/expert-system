from Operator import Operator

class OpNOT(Operator):
    """
        Represent le symbole "!"
    """
    def __init__(self):
        Operator.__init__(self, "NOT")
    def apply(self, letterLeft, letterRight):
        return not letterRight.value
