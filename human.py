from player import Player

class Human(Player):
    def __init__(self):
        self.human = True
        super().__init__()