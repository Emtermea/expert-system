class Letter:
    """
        Class qui definie une variable de nos regle
        Dans: A + B => C
        A, B et C sont des Letter
        Il contient une valeur "True" ou "False" qui servira a la resolution de l'expert system
    """
    def __init__(self, letter):
        self.letter = letter
        self.value = False

    def setTrue(self):
        """Apeller au moment du parser, potentiellement au moment ou on push dans factsBase"""
        self.value = True
