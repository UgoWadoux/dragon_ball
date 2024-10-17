class Technique:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def use(self, warrior, opponent):
        print(f"{warrior.name} uses {self.name}")
        opponent.take_damages(self.damage)


class Kamehameha(Technique):
    def __init__(self):
        super().__init__("Kamehameha", 40)


class Punch(Technique):
    def __init__(self):
        super().__init__("Punch", 15)


class Kick(Technique):
    def __init__(self):
        super().__init__("Kick", 20)


class FinalFlash(Technique):
    def __init__(self):
        super().__init__("Final Flash", 70)


class SpecialBeamCanon(Technique):
    def __init__(self):
        super().__init__("Special Beam Canon", 50)
