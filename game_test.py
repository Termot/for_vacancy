import unittest
from game_score import generate_game, get_score


class TestExample(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_func_get_score_first(self):
        game_stamps = generate_game()
        get_score(game_stamps, 1)

    def test_func_get_score_last(self):
        game_stamps = generate_game()
        get_score(game_stamps, -1)

    def test_func_get_score_all(self):
        game_stamps = generate_game()
        for i in range(len(game_stamps)):
        	get_score(game_stamps, i)


if __name__ == '__main__':
    unittest.main()
  
