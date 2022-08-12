class TennisGame:
    def __init__(self):
        self._p1_score = 0
        self._p2_score = 0

    @property        #python będzie widział "score" jako pole a dodatkowo chronimy _score
    def score(self):
        return self._calculate_score()

    def player_one_scored(self):
        self._p1_score +=1

    def player_two_scored(self):
        self._p2_score +=1

    def _calculate_score(self) -> str:
        if self.is_winner():
            return f"Game for {self.player_with_higher_score()}"

        if self.is_deuce():
            return "Deuce"

        if self.is_advantage():
            return f"Advantage {self.player_with_higher_score()}"      # TODO który gracz ?

        if self._p1_score == self._p2_score:
            return  f"{self._translate_score(self._p1_score)} All"
        return f"{self._translate_score(self._p1_score)} {self._translate_score(self._p2_score)}"

    def is_winner(self):
        return (self._p1_score >= 4 or self._p2_score >= 4 )\
            and abs(self._p1_score - self._p2_score) >= 2

    def player_with_higher_score(self):
        if self._p1_score > self._p2_score:
            return "P1"
        return "P2"

    def is_deuce(self):
        return self._p1_score >= 4 and \
               self._p2_score >= 4 and \
               self._p1_score == self._p2_score

    def is_advantage(self):
        return  self._p1_score >= 4 and \
                self._p2_score >= 4 and \
                abs(self._p1_score - self._p2_score) == 1

    def _translate_score(self, player_score):
            if player_score == 0:
                return "Love"
            elif player_score == 1:
                return "Fifteen"
            elif player_score == 2:
                return "Thirty"
            elif player_score == 3:
                return "Forty"


