import random

class Player:
    def __init__(self):
        self.name = "   "
        self.select_num = 5
        self.gesture = 5
    
    def gesture_selection(self, player):
        self.select_num = 6
        while self.select_num > 5:
            self.select_num = int(input(f""" 0: Rock, 1: Paper, 2: Scissors, 3: Lizard, 4: Spock, 5: Random
            {player.name} pick a number between 0-5: """))
            if self.select_num > 5:
                print("Incorrect input, try again!")                       
        return self.select_num

    # def gestures(self, gestures):
    #     self.gesture = " "
    #     select = True
    #     while select == True:
    #         if gestures == 0:
    #             self.gesture = "Rock"
    #             select = False
    #         elif gestures == 1:
    #             self.gesture = "Paper"
    #             select = False
    #         elif gestures == 2:
    #             self.gesture = "Scissors"
    #             select = False
    #         elif gestures == 3:
    #             self.gesture = "Lizard"
    #             select = False
    #         elif gestures == 4:
    #             self.gesture = "Spock"
    #             select = False
    #         elif gestures == 5:
    #             gestures = random.randint(0,4)
    #             select = True
    #     return self.gesture 

    def gestures(self, player):
        select = True
        while select == True:
            if player == 0:
                self.gesture_num = 0
                select = False
                print("Rock")
            elif player == 1:
                self.gesture_num = 1
                select = False
                print("Paper")
            elif player == 2:
                self.gesture_num = 2
                select = False
                print("Scissors")
            elif player == 3:
                self.gesture_num = 3
                select = False
                print("Lizard")
            elif player == 4:
                self.gesture_num = 4
                print("Spock")
                select = False
            elif player == 5:
                player = random.randint(0,4)
                select = True
        return self.gesture_num 

    def battle(self, player1, player2):
        if player1.gesture_num == 0:
            if player2.gesture_num == 1 or player2.gesture_num == 4:
                print (f"{player2.name} wins!")
                return "player2"
            elif player2.gesture_num == 0:
                print("Draw")
                return "Draw"
            else:
                print(f"{player1.name} wins!")
                return "player1"
        if player1.gesture_num == 1:
            if player2.gesture_num == 2 or player2.gesture_num == 3:
                print (f"{player2.name} wins!")
                return "player2"
            elif player2.gesture_num == 2:
                print("Draw")
                return "Draw"
            else:
                print(f"{player1.name} wins!")
                return "player1"
        if player1.gesture_num == 2:
            if player2.gesture_num == 0 or player2.gesture_num == 4:
                print (f"{player2.name} wins!")
                return "player2"
            elif player2.gesture_num == 2:
                print("Draw")
                return "Draw"
            else:
                print(f"{player1.name} wins!")
                return "player1"
        if player1.gesture_num == 3:
            if player2.gesture_num == 2 or player2.gesture_num == 0:
                print (f"{player2.name} wins!")
                return "player2"
            elif player2.gesture_num == 3:
                print("Draw")
                return "Draw"
            else:
                print(f"{player1.name} wins!")
                return "player1"
        if player1.gesture_num == 4:
            if player2.gesture_num == 3 or player2.gesture_num == 1:
                print (f"{player2.name} wins!")
                return "player2"
            elif player2.gesture_num == 4:
                print("Draw")
                return "Draw"
            else:
                print(f"{player1.name} wins!")
                return "player1"



'''
0 Rock 1,4
1 Paper 2,3
2 Scissors 0,4
3 Liz 2,0
4 Spock 3,1
'''

#get rid of boolean for gestures_selection/human/robot. 