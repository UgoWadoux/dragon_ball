from patterns.builder import WarriorBuilder
from models.fight import Fight
from patterns.singleton import WarriorManager
from patterns.observer import WarriorObserver
from patterns.state import NormalState, SuperSaiyanState

manager = WarriorManager()


def create_warrior():
    # Get user input for creating warriors
    name = input("Enter the first warrior's name: ")
    warrior_type = input("Enter the first warrior's type (Saiyan, Namekian, Android): ")
    technique = input("Enter the first warrior's technique (Kamehameha, Final Flash, Special Beam Cannon): ")
    transformation = input("Enter the first warrior's transformation: ")
    item = input("Enter the first warrior's item: ")

    # Create warriors
    warrior = WarriorBuilder(warrior_type, name) \
        .add_technique(technique) \
        .add_transformation(transformation) \
        .add_item(item) \
        .build()

    observer1 = WarriorObserver()
    warrior.attach(observer1)
    manager.add_warrior(warrior)
    return warrior


def create_opponent():
    opponent = WarriorBuilder("Android", "Mechant") \
        .add_technique("Kamehameha") \
        .add_transformation("transformation") \
        .add_item("item") \
        .build()
    observer2 = WarriorObserver()
    opponent.attach(observer2)
    manager.add_warrior(opponent)
    return opponent


def start_fight(warrior, opponent):
    combat = Fight(warrior, opponent)
    combat.start_combat()


def main():
    warriors = []

    while True:
        print("Menu \n"
              "1. Create a Warrior \n"
              "2. Train a Warrior \n"
              "3. Start a Fight \n"
              "4. Start a Tournament \n"
              "5. List Warriors \n"
              "6. Exit \n")
        choice = input("Enter your choice :\n ")

        if choice == '1' :
            warrior = create_warrior()
            warriors.append(warrior)
        elif choice == '2':
            return
        elif choice == '3':
            if not warriors:
                print("No warriors created. Please create one an try again")
                continue
            opponent = create_opponent()
            for warrior in warriors:
                i = 0
                print(f"{i}. {warrior.name}")
                i += 1
            warrior_number = input("Select a warrior Please :\n ")
            warrior_number = int(warrior_number)
            warrior = warriors[warrior_number]
            start_fight(warrior, opponent)
        elif choice == '4':
            return
        elif choice == '5':
            for warrior in warriors:
                i = 0
                print(f"{i}. {warrior.name}")
                i += 1
            continue
        elif choice == '6':
            return



if __name__ == "__main__":
    main()
