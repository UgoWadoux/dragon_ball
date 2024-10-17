class Observer:
    def update(self, event):
        pass


class WarriorObserver(Observer):
    def update(self, event):
        print(f"Event: {event}")
