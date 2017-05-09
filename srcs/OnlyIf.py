from Equal import Equal

class OnlyIf(Equal):
    """
        Class qui represente "Si et seulement si
        Donc le symbole "<=>"
    """
    def __init__(self):
        Equal.__init__(self, "ONLYIF")

    def apply(self, letterLeft, letterRight):
        return letterLeft.value == letterRight.value
