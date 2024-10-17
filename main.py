import os
from models.technique import Kamehameha, FinalFlash, SpecialBeamCanon
from patterns.builder import WarriorBuilder
from models.fight import Fight
from patterns.singleton import WarriorManager
from patterns.observer import WarriorObserver
from models.training import Training

manager = WarriorManager()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    clear_screen()
    print("=" * 40)
    print("Welcome to the Dragon Ball Game")
    print("=" * 40)
    print("Menu")
    print("1. Create a Warrior")
    print("2. Train a Warrior")
    print("3. Start a Fight")
    print("4. Start a Tournament")
    print("5. List Warriors")
    print("6. Exit")
    print("=" * 40)


def choose_technique():
    while True:
        choice_technique = input(
            "Enter the first warrior's technique (Kamehameha, Final Flash, Special Beam Cannon): ").strip()
        if choice_technique.lower() == "kamehameha":
            return Kamehameha()
        elif choice_technique.lower() == "final flash":
            return FinalFlash()
        elif choice_technique.lower() == "special beam cannon":
            return SpecialBeamCanon()
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


def create_warrior():
    clear_screen()
    print("=" * 40)
    print("Create a Warrior")
    print("=" * 40)
    name = input("Enter the first warrior's name: ")
    warrior_type = input("Enter the first warrior's type (Saiyan, Namekian, Android): ")
    technique = choose_technique()
    transformation = input("Enter the first warrior's transformation: ")
    item = input("Enter the first warrior's item: ")

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
    combat.start_fight()


def start_training(warrior):
    training = Training(warrior)
    training.train()


def choose_warrior(warriors):
    clear_screen()
    print("=" * 40)
    print("Choose a Warrior")
    print("=" * 40)
    for i, warrior in enumerate(warriors):
        print(f"{i}. {warrior.name}")
    warrior_number = int(input("Select a warrior Please: "))
    return warriors[warrior_number]


def list_warriors(warriors):
    clear_screen()
    print("=" * 40)
    print("List of Warriors")
    print("=" * 40)
    for i, warrior in enumerate(warriors):
        print(f"{i}. \n")
        warrior_display(warrior)


def warrior_display(warrior):
    print(f"Name : {warrior.name} \n"
          f"Strength : {warrior.strength} \n"
          f"HP : {warrior.hp} \n"
          f"Level : {warrior.level} \n"
          f"Experience : {warrior.experience} \n"
          f"Items : {warrior.items} \n"
          f"Techniques : {warrior.techniques} \n"
          f"Transformations : {warrior.transformations} \n"
          f"State : {warrior.state.__class__.__name__} \n")


def main():
    warriors = []

    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            warrior = create_warrior()
            warriors.append(warrior)
            input("Press Enter to continue...")
        elif choice == '2':
            if not warriors:
                print("No warriors created. Please create one and try again.")
                input("Press Enter to continue...")
                continue
            warrior = choose_warrior(warriors)
            start_training(warrior)
            input("Press Enter to continue...")
        elif choice == '3':
            if not warriors:
                print("No warriors created. Please create one and try again.")
                input("Press Enter to continue...")
                continue
            opponent = create_opponent()
            warrior = choose_warrior(warriors)
            start_fight(warrior, opponent)
            input("Press Enter to continue...")
        elif choice == '4':
            print("Starting a tournament...")
            input("Press Enter to continue...")
        elif choice == '5':
            list_warriors(warriors)
            input("Press Enter to continue...")
        elif choice == '6':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
