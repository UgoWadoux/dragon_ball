class Attacker:
    def __init__(self, techniques):
        self.techniques = techniques

    def get_techniques(self):
        return [technique.name for technique in self.techniques]

    def choose_technique(self):
        technique_names = self.get_techniques()
        print(f"Available techniques: {', '.join(technique_names)}")

        while True:
            technique_choice = input("Choose a technique to use: ")
            for technique in self.techniques:
                if technique_choice == technique.name:
                    return technique
            else:
                print("Invalid choice. Please choose a valid technique.")
