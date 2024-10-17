class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, warrior):
        print(f"{warrior.name} uses {self.name}")
        warrior.increase_strength(self.effect)