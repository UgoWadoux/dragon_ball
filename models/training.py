from patterns.observer import WarriorObserver


class Training:
    def __init__(self, warrior):
        self.warrior = warrior
        self.observers = []

    def attach_observer(self, observer):
        self.observers.append(observer)

    def detach_observer(self, observer):
        self.observers.remove(observer)

    def notify_observers(self, event):
        for observer in self.observers:
            observer.update(event)

    def train(self):
        observer = WarriorObserver()
        self.attach_observer(observer)
        print(f"{self.warrior.name} is training")
        self.warrior.increase_strength(5)
        self.warrior.gain_experience(50)
        self.notify_observers(f"{self.warrior.name} completed training.")
        self.detach_observer(observer)
