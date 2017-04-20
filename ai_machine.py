import json


class AI:

    def __init__(self):
        self.brain = {}
        self.memory = []
        self.victory = False

    def get_smarter(self):
        print("Ai is getting smarter")
        while self.memory:
            stick_count, pick = self.memory.pop()
            stick_count = str(stick_count)
            if stick_count in self.brain:  # cant find?
                self.brain[stick_count].append(pick)
            else:
                self.brain.setdefault(stick_count, [1, 2, 3, pick])

    def save_brain(self):
        with open('ai_brain.json', 'w') as outfile:
            json.dump(self.brain, outfile)
            print("Ai brain was saved")

    def load_brain(self):
        try:
            with open('ai_brain.json') as infile:
                self.brain = json.load(infile)
                print("Ai brain loaded from memory")
        except:
            print("No Ai brain in memory")
