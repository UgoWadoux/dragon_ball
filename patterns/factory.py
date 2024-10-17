from models.warrior import Warrior


class WarriorFactory:
    def create_warrior(self, warrior_type, name):
        if warrior_type == 'Saiyan':
            return Warrior(name)
        elif warrior_type == 'Namekian':
            return Warrior(name)
        elif warrior_type == 'Android':
            return Warrior(name)
        else:
            raise ValueError("Unknown warrior type")
