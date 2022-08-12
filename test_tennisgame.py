import unittest
from tennisgame import TennisGame

class TestTennisGame(unittest.TestCase):

    def setUp(self) -> None:
        self.game = TennisGame()

    def test_initial_score(self):
        initial_score = self.game.score
        self.assertEqual("Love All", initial_score)

    def test_score_15_0_when_p1_scored(self):
        self.game.player_one_scored()
        self.assertEqual("Fifteen Love", self.game.score)

    def test_score_30_0_when_p1_scored_twice(self):
        self._create_score(2,0)
        self.assertEqual("Thirty Love", self.game.score)

    def test_score_30_15_p1_scored_twice_p2_scored_once(self):
        self._create_score(2,1)
        self.assertEqual("Thirty Fifteen", self.game.score)

    def test_score_15_0_when_p2_scored_once(self):
        self._create_score(0,1)
        self.assertEqual("Love Fifteen", self.game.score)

    def test_score_15_15_when_both_scored_once(self):
        self._create_score(1, 1)
        self.assertEqual("Fifteen All", self.game.score)

    def test_score_40_0_when_p1_scored_three_times(self):
        self._create_score(3,0)
        self.assertEqual("Forty Love", self.game.score)

    def test_score_40_0_when_p1_win(self):
        self._create_score(4,0)
        self.assertEqual("Game for P1", self.game.score)

    def test_score_40_15_p2_scored_three_times_p2_scored_once(self):
        self._create_score(1,3)
        self.assertEqual("Fifteen Forty", self.game.score)

    def test_score_when_p2_win(self):
        self._create_score(0,4)
        self.assertEqual("Game for P2", self.game.score)

    def _create_score(self, player_one_score, player_two_score):
        for _ in range(player_one_score):
            self.game.player_one_scored()
        for _ in range(player_two_score):
            self.game.player_two_scored()

    def test_deuce(self):
        self._create_score(4, 4)
        self.assertEqual("Deuce", self.game.score)      # remis

    def test_deuce(self):
        self._create_score(7, 7)
        self.assertEqual("Deuce", self.game.score)  # remis

    def test_advantage_5_4_p1(self):
        self._create_score(5,4)
        self.assertEqual("Advantage P1", self.game.score)

    def test_advantage_5_4_p2(self):
        self._create_score(4, 5)
        self.assertEqual("Advantage P2", self.game.score)

    def test_advantage_5_4_p2(self):
        self._create_score(11, 12)
        self.assertEqual("Advantage P2", self.game.score)

    def test_game_for_p1_after_deuce(self):
        self._create_score(6,4)
        self.assertEqual("Game for P1", self.game.score)

    def test_game_for_p2_after_deuce(self):
        self._create_score(4,6)
        self.assertEqual("Game for P2", self.game.score)

    def test_game_for_p2_after_deuce(self):
        self._create_score(20,22)
        self.assertEqual("Game for P2", self.game.score)