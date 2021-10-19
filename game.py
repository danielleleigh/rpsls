from typing import Counter
from human import Human
from ai import AI
from player import Player

class Game:
    def __init__(self):
        self.player_one = Human()
        self.robot = AI()
        
    def run(self):
        player1counter= 0
        player2counter = 0
                
        while player1counter < 3 and player2counter < 3:
            # robot = AI()
            # robot_gesture_select = self.robot.gesture_selection()
            robot_gesture = self.robot.gestures(self.robot.gesture)

            # player_one = Human()
            player_one_select = self.player_one.gesture_selection()
            player_one_gestures = self.player_one.gestures(player_one_select)

            battle = Player()
            result = battle.battle(player_one_gestures, robot_gesture)
            if result  == "player1":
                player1counter += 1
            elif result == "player2":
                player2counter += 1






        # display_welcome
        # choose_opponents
        #  loop until a player gets to a score of 3
            # make players choose gestures
            # compare_gestures
        # display_winner()


