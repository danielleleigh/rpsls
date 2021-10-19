import random

class Player:
    def __init__(self):
        self.name = "   "
        self.select_num = []
        self.gesture = 5
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

    def gestures(self, gestures):
        self.gesture = " "
        select = True
        while select == True:
            if gestures == 0:
                self.gesture = 0
                select = False
                print("Rock")
            elif gestures == 1:
                self.gesture = 1
                select = False
                print("Paper")
            elif gestures == 2:
                self.gesture = 2
                select = False
                print("Scissors")
            elif gestures == 3:
                self.gesture = 3
                select = False
                print("Lizard")
            elif gestures == 4:
                self.gesture = 4
                print("Spock")
                select = False
            elif gestures == 5:
                gestures = random.randint(0,4)
                select = True
        return self.gesture 

    def battle(self, player1, player2):
            if player1 == 0:
                if player2 == 1 or player2 == 4:
                    print ("Rock loses")
                    return "player2"
                elif player2 == 0:
                    print("Draw")
                    return "Draw"
                else:
                    print("Rock Wins!")
                    return "player1"
            if player1 == 1:
                if player2 == 2 or player2 == 3:
                    print ("Paper loses")
                    return "player2"
                elif player2 == 2:
                    print("Draw")
                    return "Draw"
                else:
                    print("Paper Wins!")
                    return "player1"
            if player1 == 2:
                if player2 == 0 or player2 == 4:
                    print ("Scissors loses")
                    return "player2"
                elif player2 == 2:
                    print("Draw")
                    return "Draw"
                else:
                    print("Scissor wins!")
                    return "player1"
            if player1 == 3:
                if player2 == 2 or player2 == 0:
                    print ("Lizard loses")
                    return "player2"
                elif player2 == 3:
                    print("Draw")
                    return "Draw"
                else:
                    print("Lizard Wins!")
                    return "player1"
            if player1 == 4:
                if player2 == 3 or player2 == 1:
                    print ("Spock loses")
                    return "player2"
                elif player2 == 4:
                    print("Draw")
                    return "Draw"
                else:
                    print("Spock Wins!")
                    return "player1"



'''
0 Rock 1,4
1 Paper 2,3
2 Scissors 0,4
3 Liz 2,0
4 Spock 3,1
'''

#get rid of boolean for gestures_selection/human/robot. 