from patterns.state import NormalState, Dead
from models.technique import Kick, Punch, Regeneration
import random


class Warrior:
    def __init__(self, name):
        self.name = name
        self.strength = 1
        self.state = NormalState()
        self.techniques = [Punch(), Kick()]
        self.transformations = []
        self.items = {}
        self.observers = []
        self.hp = 100
        self.max_hp = 100
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100

    def add_technique(self, technique):
        self.techniques.append(technique)

    def get_techniques(self):
        return self.techniques

    def use_item(self, item_name):
        if item_name in self.items and self.items[item_name] > 0:
            item = next((i for i in self.items if i.name == item_name), None)
            if item:
                item.use(self)
                self.items[item_name] -= 1
                if self.items[item_name] == 0:
                    del self.items[item_name]
        else:
            print(f"{self.name} does not have the item {item_name}.")

    def change_state(self, state):
        self.state = state
        self.state.handle(self)
        self.notify(f"{self.name} changed state to {state.__class__.__name__}")

    def get_state(self):
        return self.state

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

    def increase_strength(self, amount):
        self.strength += amount
        self.notify(f"{self.name}'s strength increase to {self.strength}")

    def gain_experience(self, amount):
        self.experience += amount
        self.notify(f"{self.name} gained {amount} experience")
        if self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.experience = self.experience - self.experience_to_next_level
        self.level += 1
        self.experience_to_next_level *= 2
        self.increase_strength(5)
        self.increase_max_hp(10)
        self.hp = self.max_hp
        self.notify(f"{self.name} level up to {self.level}")

    def take_damages(self, technique):
        self.hp -= technique.damage
        self.notify(f"{self.name} took {technique.damage} points of damages \n "
                    f"HP : {self.hp} \n ")
        if self.hp <= 0:
            self.hp = 0
            self.change_state(Dead())
            self.notify(f"{self.name} died")
            return

    def random_technique(self):
        return random.choice(self.techniques)

    def heal(self, amount):
        self.hp += amount
        self.notify(f"{self.name} healed {amount} points of HP")
        if self.hp >= self.max_hp:
            self.hp = self.max_hp
            self.change_state(NormalState())
            self.notify(f"{self.name} is full life")

    def increase_max_hp(self, amount):
        self.max_hp += amount
        self.notify(f"{self.name} increased max HP to {self.max_hp}")

    def add_item(self, item, quantity=1):
        if item.name in self.items:
            self.items[item.name] += quantity
        else:
            self.items[item.name] = quantity
        print(f"{self.name} adds {quantity} {item.name}(s) to inventory.")


class Saiyan(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.transformations.append("Super Saiyan")

class Namekian(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.techniques = [Regeneration(), Punch(), Kick()]

class Android(Warrior):
    def __init__(self, name):
        super().__init__(name)
        self.energy = float('inf')
