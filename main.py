'''
RPSLS User Stories
Out of 65 points
Using the concepts of OOP by creating classes and using objects (instances of those classes) to interact 
with each other, create a console version of the classic game Rock Paper Scissors Lizard Spock.
Before you begin coding, write an algorithm that represents the steps necessary to play a game of 
rock, paper, scissors, lizard, Spock in a best-of-three format. By writing out the steps, it will make you 
think about every piece needed to bring the game to life. Please submit to your instructor Slack 
channel once completed for approval to start coding. Below is an example of how to get started:
- Step 1: Display the rules of the game
- Step 2: Ask how many human players will be playing
- ...
User stories:
1. (5 points): As a developer, I want to make at least 10 commits with descriptive messages.
2. (15 points): As a developer, I want to find a way to properly incorporate inheritance into my game.
3. (5 points): As a developer, I want to account for and handle bad user input, ensuring that any user input 
   is validated and reobtained if necessary.
4. (10 points): As a developer, I want to store all of the gesture options/choices in a list. I want to find
   a way to utilize the list of gestures within my code (display gesture options, assign player a gesture, etc). rf
5. (10 points): As a player, I want the correct player to win a given round based on the choices* made by 
each player.
(10 points): As a player, I want the game of RPSLS to be at minimum a ‘best of three’ to decide a 
winner.
(10 points): As a player, I want the option of a single player (human vs AI) or a multiplayer (human vs 
human) game.
* Rock crushes Scissors
Scissors cuts Paper
Paper covers Rock
Rock crushes Lizard fsbhfUHrsgh
Lizard poisons Spock
Spock smashes Scissors
Scissors decapitates Lizard
Lizard eats Paper
Paper disproves Spock
Spock vaporizes Rock


thing vs thing
'''

from game import Game

game_object = Game()
game_object.intro()
game_object.game_rules()
game_object.run()



""" from human import Human
from ai import AI
from player import Player

robot = AI()
robot_gesture_select = robot.gesture_selection()
robot_gesture = robot.gestures(robot_gesture_select)

monica = Human()
monica_gesture_select = monica.gesture_selection()
monica_gesture = monica.gestures(monica_gesture_select)

battle = Player()
battle.battle(monica_gesture, robot_gesture) """




""" gesture and gesture selection functions working properly. 
all information imports properly. next step is to create battle """