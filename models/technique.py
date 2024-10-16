class Technique:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage

    def user(self, warrior):
        print(f"{warrior.name} uses {self.name}")
