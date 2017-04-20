class AI:

    def __init__(self):
        self.brain = {}
        self.memory = []
        self.victory = False
    # consider reading the brain from file... and writing it after every game
    #dump and load from json!
    def get_smarter(self):
        while self.memory:
            stick_count, pick = self.memory.pop()
            if stick_count in self.brain:
                self.brain[stick_count].append(pick)
            else:
                self.brain.setdefault(stick_count ,[1, 2, 3, pick])