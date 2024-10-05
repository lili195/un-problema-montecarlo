class RecordVictories:
    def __init__(self):
        self.rount_number = 0
        self.victories_number = 0

    def increase(self,rount_number):
        if(rount_number == self.rount_number+1):
            self.victories_number += 1
        else:
            self.victories_number = 1