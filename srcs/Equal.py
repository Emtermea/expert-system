from Operator import Operator

class Equal(Operator):
    """
        Class qui definie un symble d'equivalence
        Correspond a '=>' ou a '<=>'
    """
    def __init__(self, typeOp):
        Operator.__init__(self, typeOp)
