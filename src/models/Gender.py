from enum import Enum

class Gender(Enum):
    MALE = 'Hombre'
    FEMALE = 'Mujer'

    def __init__(self, gender):
        self.gender = gender
    
    def get_gender(self):
        return self.gender