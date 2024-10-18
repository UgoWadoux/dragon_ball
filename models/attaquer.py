from models.form import Form

class Attacker:
    def __init__(self, techniques):
        self.techniques = techniques

    def get_techniques(self):
        return [technique.name for technique in self.techniques]

    def choose_technique(self):

        index=0
        for technique in self.techniques:
            print(f"{index}. {technique.name}")
            index+=1
        while True:
            technique_choice = input("Choose a technique to use: ")
            return self.techniques[int(technique_choice)]
