from patterns.state import NormalState

class Warrior:
    def __init__(self, name):
        self.name = name
        self.state = NormalState()
        self.techniques = []
        self.transformations = []
        self.items = []
        self.observers = []

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
