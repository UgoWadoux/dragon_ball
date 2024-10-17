class Item:
    def __init__(self, name, description, effect):
        self.name = name
        self.description = description
        self.effect = effect

    def use(self, warrior):
        print(f"{warrior.name} uses {self.name}")
        warrior.use_item(self.name)
        warrior.heal(self.effect)

class SenzuBean(Item):
    def __init__(self):
        super().__init__("Senzu Bean", "Resotore 100 HP.", 100)

class Sushi(Item):
    def __init__(self):
        super().__init__("Sushi", "Restore 20 HP.", 20)