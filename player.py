class Player:
    def __init__(self):
        self.name = "   "
        self.select_num = []
        self.gesture = " "
        self.human = True
    
    def gesture_selection(self):
        if self.human == True:
            self.select_num = int(input("Give me a number between 0-5: "))
        else:
            self.select_num = 5

    def gestures(self, gestures):
        self.gesture = " "
        if gestures == 0:
            self.gesture = "Rock"
            return self.gesture

Player()
