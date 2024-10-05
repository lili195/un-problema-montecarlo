class BonusRecordShot:
    def __init__(self):
        self.rount_number = 0
        self.bonus_number = 0

    def increase(self,rount_number):
        if(rount_number == self.rount_number+1):
            self.bonus_number += 1
        else:
            self.bonus_number = 1