from patterns.state import NormalState, SuperSaiyanState, BlessedState, ExhaustedState
from patterns.observer import WarriorObserver

class Fight:
    def __init__(self, warrior1, warrior2):
        self.warrior1 = warrior1
        self.warrior2 = warrior2
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

    def attack(self, attacker, defender):
        # Logique d'attaque
        print(f"{attacker.name} attacks {defender.name}")
        defender.change_state(BlessedState())
        self.notify_observers(f"{attacker.name} attacked {defender.name}")

    def use_special_technique(self, warrior, technique):
        # Logique d'utilisation de technique spéciale
        print(f"{warrior.name} uses {technique}")
        self.notify_observers(f"{warrior.name} used {technique}")

    def defend(self, defender):
        # Logique de défense
        print(f"{defender.name} defends")
        defender.change_state(NormalState())
        self.notify_observers(f"{defender.name} defended")

    def start_fight(self):
        # Exemple de séquence de combat
        observer = WarriorObserver()
        self.attach_observer(observer)
        self.attack(self.warrior1, self.warrior2)
        self.use_special_technique(self.warrior1, "Kamehameha")
        self.defend(self.warrior2)
        self.detach_observer(observer)
