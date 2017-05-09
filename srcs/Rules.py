class Rules:
    """
        Class qui definie une regle de logique
        Une regle de logique est sous la forme:
            A + B => C

        Dans notre code, un regle est sous de la forme:
            Expression Left, Equal, Expression Right
    """
    def __init__(self, leftExp, equal, rightExp):
        self.leftExp = leftExp
        self.equal = equal
        self.rightExp = rightExp
