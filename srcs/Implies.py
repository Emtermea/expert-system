from Equal import Equal

class Implies(Equal):
    """
        Class qui represente "implique"
        A => B
        A "implique" B
    """
    def __init__(self):
        Equal.__init__(self, "IMPLIES")

    def apply(self, letterLeft, letterRight):
        if (letterLeft.value == True and letterRight.value == False):
            return False
        else:
            return True
