# game_testing_suite/ai_exploratory_testing/game.py

class Game:
    def __init__(self):
        self.player_position = [0, 0]

    def move_player(self, x, y):
        self.player_position[0] += x
        self.player_position[1] += y
        print(f"Player moved to {self.player_position}")

    def jump_player(self):
        print("Player jumped!")

    def crouch_player(self):
        print("Player crouched!")
