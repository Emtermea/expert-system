class Expression:
    """
        Class qui definie une expression
        Example: (A + B) | (C | D)

        Une expression represente un arbre binaire
        L'example ce dessus devien alors:
                |
              // \\
           +         +
         // \\     // \\
        A     B   C     D
    """

    def __init__(self, node):
        self.node = node
