class AI:

    def __init__(self):
        self.brain = {}
        self.memory = []
        self.victory = False
    # consider reading the brain from a file... and writing it after every game
    # that way the ai learns to never lose!!!!!
    #dump and load from json!
    def get_smarter(self):
        while len(self.memory) > 0:
            stick_count, pick = self.memory.pop()
            if stick_count in self.brain:
                self.brain[stick_count].append(pick)
            else:
                self.brain.setdefault(stick_count ,[1, 2, 3, pick])