import random
from ai_machine import AI


class Game:

    def __init__(self):
        self.stix = 0
        self.curr_player = "Player 1"
        self.waiting_player = ""
        self.machine = None
        self.victor = ""
        self.valid_turns = [1, 2, 3]

    def game_title(self):
        print("\n" + "\t"*4 + "*** Welcome to game of sticks ***")
        print("The object of the game is to pick up sticks, 1-3 at a time, but don't be the one to pick up the last one!\n")

    def get_from_user(self, msg):
        user_input = ""
        while not user_input and not len(user_input):
            user_input = input("{} ".format(msg))
        return user_input.lower()

    def get_stix(self):
        while True:
            stick_count = self.get_from_user("\nHow many sticks would you like to play with?")
            if stick_count.isdigit():
                stick_count = int(stick_count)
                if stick_count >= 10 and stick_count <= 100:
                    return stick_count
            print("\nTry again...\n")

    def get_player(self):
        choice = ""
        while not choice and not len(choice):
            choice = self.get_from_user("\nWould you like to play against an AI (Y/n)?")
            if choice[0] == 'y':
                self.machine = AI()
                self.machine.load_brain()
            elif choice[0] == 'n':
                self.machine = None
            else:
                print("... Lets try that again")

    def take_turn(self):
        print("\n* There are {} sticks left *".format(self.stix))
        valid = False
        while not valid:
            turn = self.get_from_user("\n{}, pick a stick (1-3):".format(self.curr_player))
            if turn.isdigit():
                turn = int(turn)
                if turn in self.valid_turns:
                    self.stix -= turn
                    valid = True

    def winner(self, player):
        # Can rework
        self.victor = player
        print("\t  {} Wins".format(self.victor))

    def is_game_over(self):
        if self.stix <= 1:
            print("\n\t!!! Game Over !!!")
            if self.stix == 1:
                self.winner(self.curr_player)
            elif self.stix < 1:
                self.winner(self.waiting_player)
            return True
        return False

    def game_board(self):
        print("There are {} sticks remaining\n".format(self.stix))

    def play(self):
        self.stix = self.get_stix()
        coin = random.randint(1, 2)
        if not self.machine:
            while not self.is_game_over():
                if coin % 2 == 0:
                    self.curr_player, self.waiting_player = "Player 1", "Player 2"
                else:
                    self.curr_player, self.waiting_player = "Player 2", "Player 1"
                self.take_turn()
                coin += 1
        else:
            while not self.is_game_over():
                if coin % 2 == 0:
                    self.curr_player, self.waiting_player = "Player 1", "Machine"
                    self.take_turn()
                else:
                    self.curr_player, self.waiting_player = "Machine", "Player 1"
                    if str(self.stix) in self.machine.brain:
                        pick = random.choice(self.machine.brain[str(self.stix)])
                    else:
                        pick = random.randint(1, 3)

                    print("\n >> AI picked up {} <<".format(pick))
                    self.machine.memory.append((str(self.stix), pick))
                    self.stix -= pick
                coin += 1

        play_again = self.get_from_user("\nWant to play again (Y/n)?")
        if play_again[0] == 'y':
            if self.machine:
                if self.victor == "Machine":
                    self.machine.get_smarter()
                else:
                    self.machine.memory = []
            self.play()
        else:
            if self.machine:

            print('\nBye, Felicia')
            exit()
