from typing import Counter
from human import Human
from ai import AI
from player import Player
import time



class Game:
    def __init__(self):
        self.player_one = Human()
        self.player_one.name = "Player 1"
        self.player_two = Human()
        self.player_two.name = "Player 2"

    def intro (self):
        print("Welcome")
        time.sleep(1)
        print("To the")
        time.sleep(1)
        print("Thunderdome!")

    def game_rules (self):
            print("Rock, Paper, Scissors, Lizard, Spock (RPSLS) is played best 2 out of 3. Each gesture correlates with a number.")
            time.sleep(1)
            print("Rock is 0, Paper is 1, Scissors is 2, Lizard is 3, Spock is 4. To pick a number randomly, input the number 5. ")
            time.sleep(1)
            print("Here is a breakdown of who beats who: ")
            time.sleep(1)
            print("Rock crushes Scissors and Lizards.")        
            time.sleep(1)
            print("Scissors cut paper and decapitates Lizard.")     
            time.sleep(1)
            print("Paper covers rock and disproves Spock.")      
            time.sleep(1)
            print("Lizard eats paper and poisons Spock.")     
            time.sleep(1)
            print("Spock smashes scissors and vaporizes Rock.")     
            time.sleep(1) 

    def run(self):
        user_selection = int(input("Press 1 for single plater. Press 2 for two player: "))
        player1counter = 0
        player2counter = 0
        if user_selection == 1:
            self.player_two.select_num = 5
            while player1counter < 3 and player2counter < 3:
                self.player_one.gesture_selection(self.player_one)
                self.player_one.gesture_num = self.player_one.gestures(self.player_one.select_num)
                if self.player_two.select_num == 5:
                    self.player_two.gesture_num = self.player_two.gestures(self.player_two.select_num)
                else:
                    self.player_two.gesture_selection(self.player_two)
                    self.player_two.gesture_num = self.player_two.gestures(self.player_two.select_num)
                battle = Player()
                result = battle.battle(self.player_one, self.player_two)
                # changed player_one_gestures and player_two_gestures to player_one and player_two, hoping to call their name like player_one.name in the battle
                if result  == "player1":
                    player1counter += 1
                    if player1counter == 3:
                        print(f"{self.player_one.name} wins the game!")
                elif result == "player2":
                    player2counter += 1
                    if player2counter == 3:
                        print(f"{self.player_two.name} wins the game!")
                        
                        
"""     You should only have a "player_one" and "player_two" variables.
    Then when the user chooses single player or multiplayer, we then determine what to set player_two equal to.
    For example if the select single player we should set "player_two" equal to a AI object.
    If they choose multiplayer then we should set "player_two" equal to a Human object.
    Then in your "run" method you no longer need to have your if statement checking the "user_selection"
    It doesnt matter what player_two is set equal to becuase both AI and Human both have the same method to be called when selecting a gesture.   """       

         
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

