from player import Player

class AI(Player):
    def __init__(self):
        self.human = False

AI(Player)
""" Exception has occurred: TypeError       (note: full exception trace is shown but execution is paused at: <module>)
__init__() takes 1 positional argument but 2 were given
  File "/Users/danielle/Desktop/DevCodeCamp/rpsls/ai.py", line 7, in <module> (Current frame)
    AI(Player)
  File "/Users/danielle/Desktop/DevCodeCamp/rpsls/main.py", line 41, in <module>
    from ai import AI """