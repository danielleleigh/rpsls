import random

class Player:
    def __init__(self):
        self.name = "   "
        self.select_num = []
        self.gesture = " "
        self.human = True
    
    def gesture_selection(self):
        self.select_num = 6
        while self.select_num > 5:
            if self.human == True:
                self.select_num = int(input("Give me a number between 0-5: "))
                if self.select_num > 5:
                    print("Incorrect input, try again")
            elif self.human == False:
                self.select_num = 5                   
        return self.select_num

    def gestures(self, gestures):
        self.gesture = " "
        select = True
        while select == True:
            if gestures == 0:
                self.gesture = "Rock"
                select = False
            elif gestures == 1:
                self.gesture = "Paper"
                select = False
            elif gestures == 2:
                self.gesture = "Scissors"
                select = False
            elif gestures == 3:
                self.gesture = "Lizard"
                select = False
            elif gestures == 4:
                self.gesture = "Spock"
                select = False
            elif gestures == 5:
                gestures = random.randint(0,4)
                select = True
        return self.gesture 

    def battle(self, player1, player2):
        self.rock = 0
        self.paper = 1
        self.scissors = 2
        self.lizard = 3
        self.spock = 4
        if self.rock < self.paper:
            print("Rock wins!")
        elif self.rock < self.lizard:
            print("Rock wins!")
        