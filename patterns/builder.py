from patterns.factory import WarriorFactory


class WarriorBuilder:
    def __init__(self, warrior_type, name):
        self.warrior = WarriorFactory().create_warrior(warrior_type, name)

    def add_technique(self, technique):
        self.warrior.add_technique(technique)
        return self

    def add_transformation(self, transformation):
        self.warrior.transformations.append(transformation)
        return self

    def add_item(self, item):
        self.warrior.items.append(item)
        return self

    def build(self):
        return self.warrior
