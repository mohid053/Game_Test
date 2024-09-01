from ai_exploratory_testing.game import Game
from ai_exploratory_testing.ai_bot import AIBot
from framework.test_runner import run_tests

def main():
    print("Running automated tests...")
    run_tests()

    print("\nRunning AI exploratory testing...")
    game = Game()
    bot = AIBot(game)
    bot.explore()

if __name__ == "__main__":
    main()
