from models.warrior import Warrior

class WarriorFactory:
    def create_warrior(self, warrior_type, name):
        if warrior_type == 'Saiyan':
            return Saiyan(name)
        elif warrior_type == 'Namekian':
            return Namekian(name)
        elif warrior_type == 'Android':
            return Android(name)
        else:
            raise ValueError("Unknown warrior type")
