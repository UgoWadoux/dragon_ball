class WarriorDecorator:
    def __init__(self, warrior):
        self.warrior = warrior

    def add_transformation(self, transformation):
        self.warrior.transformations.append(transformation)

    def add_item(self, item):
        self.warrior.items.append(item)


class SuperSaiyanDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_transformation("Super Saiyan")


        self.add_item("Item")
class SenzuBeanDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_item("Senzu Bean")

class SushiDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_item("Sushi")
