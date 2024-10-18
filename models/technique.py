class Technique:
    def __init__(self, name, damage, animation):
        self.name = name
        self.damage = damage
        self.animation = animation

    def \
        use(self, warrior, opponent):
        print(f"{warrior.name} uses {self.name}")
        opponent.take_damages(self.damage)



class Kamehameha(Technique):
    def __init__(self):
        super().__init__("Kamehameha", 40, [ """
            O
           /|
           / \\
          """,
            """
            O
            |\\===0
           / \\
          """,
            """
            O
            |\\=======0
           / \\
          """,
            """
            O
            |\\==========0
           / \\
          """])


class Punch(Technique):
    def __init__(self):
        super().__init__("Punch", 15, [ """
            O
           /|
           / \\
          """,
            """
            O
            |
           / \\
          """,
            """
            O
            |/
           / \\
          """,
           ])


class Kick(Technique):
    def __init__(self):
        super().__init__("Kick", 20, ["""
            O
           /|
           / \\
          """,
            """
            O
           /|
            | 
          """,
            """
            O
           /|/
            |
          """,])


class FinalFlash(Technique):
    def __init__(self):
        super().__init__("Final Flash", 70,[ """
            O
           /|
           / \\
          """,
            """
            O
            |\\***O
           / \\
          """,
            """
            O  
            |\\*******O
           / \\
          """,
            """
            O 
            |\\**********O
           / \\
          """] )


class SpecialBeamCanon(Technique):
    def __init__(self):
        super().__init__("Special Beam Canon", 50, [ """
            O
           /|
           / \\
          """,
            """
            O  
            |\\%%%0
           / \\
          """,
            """
            O  
            |\\%%%%%%%0
           / \\
          """,
            """
            O  
            |\\%%%%%%%%%%0
           / \\
          """])

class Regeneration(Technique):
    def __init__(self):
        super().__init__("Regeneration", 0, [''])
