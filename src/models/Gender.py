from enum import Enum

class Gender(Enum):
    MALE = 'm'
    FEMALE = 'f'

    def __init__(self, gender):
        self.gender = gender
    
    def get_gender(self):
        return self.gender