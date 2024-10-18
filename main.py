import os

from models.item import SenzuBean
from models.technique import Kamehameha, FinalFlash, SpecialBeamCanon
from patterns.builder import WarriorBuilder
from models.fight import Fight
from patterns.singleton import WarriorManager
from patterns.observer import WarriorObserver
from models.training import Training
from models.form import Form
from patterns.decorator import SenzuBeanDecorator, SushiDecorator

manager = WarriorManager()


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_menu():
    clear_screen()
    print("========================================")
    print("|   Welcome to the Dragon Ball Game    |")
    print("=" * 40)
    print("""|                                      |
|       ⠀⠀⠀⠀⠀⢀⣀⣤⣴⣶⣶⣶⣶⣆⢰⣦⣤⣀⡀⠀⠀⠀⠀⠀⠀      |
|   ⠀⠀⠀⠀⠀⢀⣠⣶⣿⣿⣿⣿⣿⡿⢿⣿⣿⠀⣿⣿⣿⣿⣶⣄⡀⠀⠀⠀⠀⠀     |
|   ⠀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⠃⠀⣿⠿⠛⠀⠻⢿⣿⣿⣿⣿⣿⣦⠀⠀⠀⠀     |
|   ⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠃⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣷⡄⠀⠀     |
|   ⠀⢠⣿⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⢛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠀     |
|   ⠀⣾⣿⣿⣿⣿⣿⠿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢹⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀     |
|   ⢸⣿⣿⣿⣿⣛⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⡆⢠⡈⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     |
|   ⢸⣿⣿⣿⣿⣟⣉⣁⠀⠀⠀⠀⠀⠀⠀⠀⣻⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     |
|   ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠇⠀⠀⣠⣴⣿⣿⠈⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇     |
|   ⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠙⣿⣿⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇     |
|   ⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡀⠀⠀⠀⠀⠈⠁⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀     |
|   ⠀⠈⢿⣿⣿⣿⣿⣿⠿⢿⣿⡇⠀⠀⠀⠀⠀⣤⠀⢸⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀     |
|   ⠀⠀⠈⢿⣿⣿⣿⠁⣴⣾⡿⠁⠀⠀⠀⠀⠀⠘⡇⢸⣿⣿⣿⣿⣿⣿⡟⠁⠀⠀     |
|   ⠀⠀⠀⠀⠙⢿⣿⡀⠿⣿⡧⠀⠀⠀⠀⠀⠀⢠⡄⢸⣿⣿⣿⣿⡿⠋⠀⠀⠀⠀     |
|   ⠀⠀⠀⠀⠀⠀⠙⠻⢶⣤⣤⣾⠀⠀⠀⠀⢠⣼⡇⢸⣿⡿⠟⠋⠀⠀⠀⠀⠀⠀     |
|   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠙⠃⠀⠀⠀⠠⠿⠟⠃⠈⠉⠀⠀⠀⠀⠀⠀     ⠀⠀⠀|""")
    print("========================================")
    print("|                MENU                  |")
    print("========================================")
    print("|       1. Create a Warrior            |")
    print("|       2. Train a Warrior             |")
    print("|       3. Start a Fight               |")
    print("|       4. Start a Tournament          |")
    print("|       5. List Warriors               |")
    print("|       6. Exit                        |")
    print("=" * 40)


def choose_technique():
    while True:
        form = Form()
        return form.display(title="Choose technique", choices=["kamehameha",
                                                               "final flash",
                                                               "special beam canon"], functions=[lambda: Kamehameha(),
                                                                                                 lambda: FinalFlash(),
                                                                                                 lambda: SpecialBeamCanon()])


def choose_item(warrior):
    while True:
        form = Form()
        return form.display(title="Choose first item", choices=["senzu bean",
                                                                "sushi"],
                            functions=[lambda: SenzuBeanDecorator(warrior),
                                       lambda: SushiDecorator(warrior)])


def choose_warrior_type():
    while True:
        form = Form()
        return form.display(title="Choose type", choices=["Saiyan",
                                                          "Namekian",
                                                          "Android"], functions=[lambda: "Saiyan",
                                                                                 lambda: "Namekian",
                                                                                 lambda: "Android"])


def create_warrior():
    clear_screen()
    print("=" * 40)
    print("Create a Warrior")
    print("=" * 40)
    name = input("Enter the first warrior's name: ")
    warrior_type = choose_warrior_type()
    technique = choose_technique()
    # transformation = input("Enter the first warrior's transformation: ")

    warrior = WarriorBuilder(warrior_type, name) \
        .add_technique(technique) \
        .build()
    choose_item(warrior)
    observer1 = WarriorObserver()
    warrior.attach(observer1)
    manager.add_warrior(warrior)
    return warrior


def create_opponent():
    opponent = WarriorBuilder("Android", "Mechant") \
        .add_technique(SpecialBeamCanon()) \
        .add_transformation("transformation") \
        .build()
    SushiDecorator(opponent)
    observer2 = WarriorObserver()
    opponent.attach(observer2)
    manager.add_warrior(opponent)
    return opponent


def create_goku():
    goku = WarriorBuilder("Saiyan", "Goku") \
        .add_technique(Kamehameha()) \
        .add_transformation("") \
        .build()
    SenzuBeanDecorator(goku)
    observer = WarriorObserver()
    goku.attach(observer)
    manager.add_warrior(goku)
    return goku


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
    opponent = create_opponent()
    create_goku()
    warriors = manager.list_warriors()
    while True:
        print_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            create_warrior()
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

            warrior = choose_warrior(warriors)
            start_fight(warrior, opponent)
        elif choice == '4':
            print("Starting a tournament...")
            input("Press Enter to continue...")
        elif choice == '5':
            list_warriors(manager.warriors)
            input("Press Enter to continue...")
        elif choice == '6':
            print("Exiting the game...")
            break
        else:
            print("Invalid choice. Please try again.")
            input("Press Enter to continue...")


if __name__ == "__main__":
    main()
