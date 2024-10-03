from enum import Enum

class Score(Enum):
    CENTER = 10
    INTERMEDIATE = 9
    OUTSIDE = 8
    ERROR = 0

    def __init__(self, Score):
        self.score = Score