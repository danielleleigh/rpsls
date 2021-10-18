from human import Human
from ai import AI
from player import Player

class Game:
    def __init__(self):
        self.player_one = None
        self.player_two = None
        
    def run(self):
        robot = AI()
        robot_gesture_select = robot.gesture_selection()
        robot_gesture = robot.gestures(robot_gesture_select)

        monica = Human()
        monica_gesture_select = monica.gesture_selection()
        monica_gesture = monica.gestures(monica_gesture_select)

        battle = Player()
        battle.battle(monica_gesture, robot_gesture)






        # display_welcome
        # choose_opponents
        #  loop until a player gets to a score of 3
            # make players choose gestures
            # compare_gestures
        # display_winner()


