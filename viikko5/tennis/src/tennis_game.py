class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score = 0
        self.player2_score = 0
        self.score_names = ["Love", "Fifteen", "Thirty", "Forty"]

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.player1_score = self.player1_score + 1
        else:
            self.player2_score = self.player2_score + 1

    def get_score(self):
        if self.player1_score == self.player2_score:
            return self.get_tie_text()
        if self.player1_score >= 4 or self.player2_score >= 4:
            return self.get_lead_text()
        score_text = self.score_names[self.player1_score] + \
            "-" + self.score_names[self.player2_score]
        return score_text

    def get_lead_text(self):
        if self.player1_score > self.player2_score:
            leading_player = self.player1_name
        else:
            leading_player = self.player2_name
        score_text = ""
        match_won = bool(abs(self.player1_score - self. player2_score) > 1)
        if match_won:
            score_text = "Win for " + leading_player
        else:
            score_text = "Advantage " + leading_player
        return score_text

    def get_tie_text(self):
        if self.player1_score >= 4:
            score_text = "Deuce"
        else:
            score_text = self.score_names[self.player1_score] + "-All"
        return score_text
