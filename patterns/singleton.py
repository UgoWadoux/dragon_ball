class WarriorManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WarriorManager, cls).__new__(cls)
            cls._instance.warriors = []
        return cls._instance

    def add_warrior(self, warrior):
        self.warriors.append(warrior)

    def get_warrior(self, name):
        for warrior in self.warriors:
            if warrior.name == name:
                return warrior
        return None
