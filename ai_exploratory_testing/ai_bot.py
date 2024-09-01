# game_testing_suite/ai_exploratory_testing/ai_bot.py

import random

class AIBot:
    def __init__(self, game):
        self.game = game

    def explore(self):
        actions = ['move_right', 'move_left', 'jump', 'crouch']
        for _ in range(10):  # Simulate 10 random actions
            action = random.choice(actions)
            print(f"AI Bot performing action: {action}")
            self.perform_action(action)

    def perform_action(self, action):
        if action == 'move_right':
            self.game.move_player(1, 0)
        elif action == 'move_left':
            self.game.move_player(-1, 0)
        elif action == 'jump':
            self.game.jump_player()
        elif action == 'crouch':
            self.game.crouch_player()
# game_testing_suite/ai_exploratory