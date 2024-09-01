# game_testing_suite/framework/test_runner.py

import unittest

def run_tests():
    """Discover and run all tests."""
    loader = unittest.TestLoader()
    suite = loader.discover('test_cases')

    runner = unittest.TextTestRunner()
    runner.run(suite)

if __name__ == "__main__":
    run_tests()
