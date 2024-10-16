from patterns.builder import WarriorBuilder
from patterns.singleton import WarriorManager
from patterns.observer import WarriorObserver
from patterns.state import NormalState, SuperSaiyanState

def main():
    manager = WarriorManager()

    # Create a warrior
    warrior = WarriorBuilder("Saiyan", "Goku") \
        .add_technique("Kamehameha") \
        .add_transformation("Super Saiyan") \
        .add_item("Senzu Bean") \
        .build()

    # Add observer
    observer = WarriorObserver()
    warrior.attach(observer)

    # Add warrior to manager
    manager.add_warrior(warrior)

    # Change state
    warrior.change_state(SuperSaiyanState())

if __name__ == "__main__":
    main()
