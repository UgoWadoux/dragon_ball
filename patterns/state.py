class WarriorState:
    def handle(self, warrior):
        pass

    def is_instance(self, warrior_state):
        return isinstance(self, warrior_state)


class NormalState(WarriorState):
    def handle(self, warrior):
        print(f"{warrior.name} is in Normal state")


class SuperSaiyanState(WarriorState):
    def handle(self, warrior):
        print(f"{warrior.name} is in Super Saiyan state")


class BlessedState(WarriorState):
    def handle(self, warrior):
        print(f"{warrior.name} is in Blessed state")


class ExhaustedState(WarriorState):
    def handle(self, warrior):
        print(f"{warrior.name} is in Exhausted state")


class Dead(WarriorState):
    def handle(self, warrior):
        print(f"{warrior.name} is dead")
