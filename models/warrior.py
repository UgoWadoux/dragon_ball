from patterns.state import NormalState

class Warrior:
    def __init__(self, name):
        self.name = name
        self.strength = 1
        self.state = NormalState()
        self.techniques = []
        self.transformations = []
        self.items = []
        self.observers = []
        self.hp = 100
        self.level = 1
        self.experience = 0
        self.experience_to_next_level = 100

    def change_state(self, state):
        self.state = state
        self.state.handle(self)
        self.notify(f"{self.name} changed state to {state.__class__.__name__}")

    def attach(self, observer):
        self.observers.append(observer)

    def detach(self, observer):
        self.observers.remove(observer)

    def notify(self, event):
        for observer in self.observers:
            observer.update(event)

    def increase_strength(self, amount):
        self.strength =+ amount
        self.notify(f"{self.name}'s strength increase to {self.strength}")

    def gain_experience(self, amount):
        self.experience =+ amount
        self.notify(f"{self.name} gained {amount} experience")
        if self.experience >= self.experience_to_next_level:
            self.level_up()

    def level_up(self):
        self.experience = self.experience - self.experience_to_next_level
        self.level += 1
        self.experience_to_next_level *= 2
        self.increase_strength(5)
        self.notify(f"{self.name} level up to {self.level}")

    def take_damages(self, damages):
        self.hp -= damages
        self.notify(f"{self.name} took {damages} points of damage \n "
                    f"HP : {self.hp} \n ")
        if self.hp <= 0:
            self.hp = 0
            self.notify(f"{self.name} died")
            return
