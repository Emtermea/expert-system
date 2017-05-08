class Letter:
    def __init__(self, letter):
        self.letter = letter
        self.value = False

    # Apeller au moment du parser, potentiellement au moment ou on push dans factsBase
    def setTrue(self):
        self.value = True
