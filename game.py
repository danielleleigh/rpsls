from typing import Counter
from human import Human
from ai import AI
from player import Player
import time

class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_two = Human()
        self.robot = AI()

    def intro (self):
        print("Welcome")
        time.sleep(1)
        print("To the")
        time.sleep(1)
        print("Thunderdome!")

    def game_rules (self):
            print("RPSLS is played best 2 out of 3.")
            time.sleep(1)
            print("Here is a breakdown of who beats who: ")
            time.sleep(2)
            print("Rock crushes Scissors and Lizards.")        
            time.sleep(2)
            print("Scissors cut paper and decapitates Lizard.")     
            time.sleep(2)
            print("Paper covers rock and disproves Spock.")      
            time.sleep(2)
            print("Lizard eats paper and poisons Spock.")     
            time.sleep(2)
            print("Spock smashes scissors and vaporizes Rock.")     
            time.sleep(2)

    def run(self):
        user_selection = int(input("Press 1 for single plater. Press 2 for two player: "))
        player1counter = 0
        player2counter = 0
        if user_selection == 1:
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
        elif user_selection == 2:
            while player1counter < 3 and player2counter < 3:
                # robot = AI()
                # robot_gesture_select = self.robot.gesture_selection()
                player_two_select = self.player_two.gesture_selection()
                player_two_gestures = self.player_two.gestures(player_two_select)

                # player_one = Human()
                player_one_select = self.player_one.gesture_selection()
                player_one_gestures = self.player_one.gestures(player_one_select)

                battle = Player()
                result = battle.battle(player_one_gestures, player_two_gestures)
                if result  == "player1":
                    player1counter += 1
                elif result == "player2":
                    player2counter += 1

    # def run(self):
    #     player1counter= 0
    #     player2counter = 0
                
    #     while player1counter < 3 and player2counter < 3:
    #         # robot = AI()
    #         # robot_gesture_select = self.robot.gesture_selection()
    #         robot_gesture = self.robot.gestures(self.robot.gesture)

    #         # player_one = Human()
    #         player_one_select = self.player_one.gesture_selection()
    #         player_one_gestures = self.player_one.gestures(player_one_select)

    #         battle = Player()
    #         result = battle.battle(player_one_gestures, robot_gesture)
    #         if result  == "player1":
    #             player1counter += 1
    #         elif result == "player2":
    #             player2counter += 1






        # display_welcome
        # choose_opponents
        #  loop until a player gets to a score of 3
            # make players choose gestures
            # compare_gestures
        # display_winner()

