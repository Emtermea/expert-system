class Implies(Equal):
    def __init__(self):
        Equal.__init__(self, "IMPLIES")

    def apply(self, letterLeft, letterRight):
        if (letterLeft.value == True and letterRight.value == False):
            return False
        else:
            return True
