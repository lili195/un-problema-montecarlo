from enum import Enum

class Score(Enum):
    CENTER = 10
    INTERMEDIATE = 9
    OUTSIDE = 8
    ERROR = 0

    def __init__(self, Score):
        self.score = Score

# class Score:
#     def __init__(self):
#         self.team_scores = {"Team A": 0, "Team B": 0}

#     def add_points(self, team, points):
#         self.team_scores[team] += points

#     def get_winner(self):
#         # Retorna el equipo ganador
#         if self.team_scores["Team A"] > self.team_scores["Team B"]:
#             return "Team A"
#         elif self.team_scores["Team B"] > self.team_scores["Team A"]:
#             return "Team B"
#         else:
#             return "Empate"
