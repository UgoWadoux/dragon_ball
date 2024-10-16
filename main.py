from patterns.builder import WarriorBuilder
from models.fight import Fight
from patterns.singleton import WarriorManager
from patterns.observer import WarriorObserver
from patterns.state import NormalState, SuperSaiyanState
from models.training import Training
import pygame
import  sys


manager = WarriorManager()
# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Dragon Ball Management")

# Fonts
font = pygame.font.Font(None, 36)
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
    combat.start_fight()

def start_training(warrior):
    training = Training(warrior)
    training.train()

def choose_warrior(warriors):
    for warrior in warriors:
        i = 0
        print(f"{i}. {warrior.name}")
        i += 1
    warrior_number = input("Select a warrior Please :\n ")
    warrior_number = int(warrior_number)
    return warriors[warrior_number]

def main():
    warriors = []

    while True:
        screen.fill(WHITE)
        menu_text = font.render("Menu:", True, BLACK)
        screen.blit(menu_text, (50, 50))

        option1_text = font.render("1. Create a warrior", True, BLACK)
        screen.blit(option1_text, (50, 100))

        option2_text = font.render("2. Train a warrior", True, BLACK)
        screen.blit(option2_text, (50, 150))

        option3_text = font.render("3. Start a combat", True, BLACK)
        screen.blit(option3_text, (50, 200))

        option4_text = font.render("4. Start a tournament", True, BLACK)
        screen.blit(option4_text, (50, 250))

        option5_text = font.render("5. Exit", True, BLACK)
        screen.blit(option5_text, (50, 300))

        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    warrior = create_warrior()
                    warriors.append(warrior)
                elif event.key == pygame.K_2:
                    if not warriors:
                        print("No warriors created yet.")
                        continue
                    warrior = choose_warrior(warriors)
                    if warrior:
                        start_training(warrior)
                    else:
                        print("Warrior not found.")
                elif event.key == pygame.K_3:
                    if not warriors:
                        print("No warriors created. Please create one an try again")
                        continue
                    opponent = create_opponent()
                    warrior = choose_warrior(warriors)
                    start_fight(warrior, opponent)
                elif event.key == pygame.K_4:
                        print("Not enough warriors to start a tournament.")
                        continue
                elif event.key == pygame.K_5:
                    for warrior in warriors:
                        i = 0
                        print(f"{i}. {warrior.name}")
                        i += 1
                    continue
                elif event.key == pygame.K_6:
                    pygame.quit()
                    sys.exit()
                else:
                    print("Invalid choice. Please try again.")
        # print("Menu \n"
        #       "1. Create a Warrior \n"
        #       "2. Train a Warrior \n"
        #       "3. Start a Fight \n"
        #       "4. Start a Tournament \n"
        #       "5. List Warriors \n"
        #       "6. Exit \n")
        # choice = input("Enter your choice :\n ")
        #
        # if choice == '1' :
        #     warrior = create_warrior()
        #     warriors.append(warrior)
        # elif choice == '2':
        #     warrior = choose_warrior(warriors)
        #     start_training(warrior)
        #     continue
        # elif choice == '3':
        #     if not warriors:
        #         print("No warriors created. Please create one an try again")
        #         continue
        #     opponent = create_opponent()
        #     warrior = choose_warrior(warriors)
        #     start_fight(warrior, opponent)
        # elif choice == '4':
        #     return
        # elif choice == '5':
        #     for warrior in warriors:
        #         i = 0
        #         print(f"{i}. {warrior.name}")
        #         i += 1
        #     continue
        # elif choice == '6':
        #     return



if __name__ == "__main__":
    main()
