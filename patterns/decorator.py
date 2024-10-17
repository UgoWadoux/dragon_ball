from models.item import SenzuBean, Sushi

class WarriorDecorator:
    def __init__(self, warrior):
        self.warrior = warrior

    def add_transformation(self, transformation):
        self.warrior.transformations.append(transformation)

    def add_item(self, item, quantity):
        self.warrior.add_item(item, quantity)

    def use_item(self, item_name):
        for item in self.warrior.items:
            if item.name == item_name:
                item.use(self.warrior)
                return
        print(f"{self.warrior.name} does not have the item {item_name}.")


class SuperSaiyanDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_transformation("Super Saiyan")


class SenzuBeanDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_item(SenzuBean(), 1)


class SushiDecorator(WarriorDecorator):
    def __init__(self, warrior):
        super().__init__(warrior)
        self.add_item(Sushi(), 1)
