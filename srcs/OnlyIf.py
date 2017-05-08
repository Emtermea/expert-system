class OnlyIf(Equal):
    def __init__(self):
        Equal.__init__(self, "ONLYIF")

    def apply(self, letterLeft, letterRight):
        return letterLeft.value == letterRight.value
