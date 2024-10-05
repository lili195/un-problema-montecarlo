class Simulation:

    def __init__(self, teamA, teamB):
        self.teamA = teamA
        self.teamB = teamB
        self.rount_count = 0
        self.champion = None


    def star_rount(self):
        self.rount_number += 1

        self.simulate_shots(self.teamA)
        self.simulate_shots(self.teamB)
        players = self.teamA.players + self.teamB.players
        champion_player = self.get_champion_player(players)
        champion_player.won_round()

    def get_champion_player(self, players):
        max_score_player = max(players, key=lambda x: x.round_score)
        max_score_players = [player for player in players if player.round_score == max_score_player.round_score]

        if len(max_score_players) > 1: 
            players = self.solve_tie_players(max_score_players)
            max_score_player= self.get_champion_player(players)

        return max_score_player

    def get_champion_team(self):
        if self.rount_count == 10:
            if self.teamA.score < self.teamB.score:
                self.champion = self.teamB
            elif self.teamA.score > self.teamB.score:
                self.champion = self.teamA
            else:
                self.champion = None 
            players = self.teamA.players + self.teamB.players 
            max(players, key=lambda x: x.rounds_won)

        else:
            self.init_players    

    def init_players(self):
        for player in self.teamA.players + self.teamB.players:
            player.luck = player.generate_luck()
            player.round_score = 0
            player.add_wear()
            player.current_resistance = player.resistance
        
    def additional_shoot(self,team):
        lucky_player = max(team.players, key=lambda x: x.luck)
        if lucky_player.bonus_record_shot.bonus_number == 2:
            score = lucky_player.simulate_shoot()
            team.increase_score(score)
        score = lucky_player.simulate_shoot()
        team.increase_score(score)
        lucky_player.record_bonus(self.rount_count)              

    def simulate_shots(self, team):
        for player in team.players:
            while player.can_continue_shooting():
                score = player.toShot()
                player.add_roundScore(score)
                team.update_score(score)
        
        self.additional_shoot(team)

    def solve_tie_players(self,players):
        for player in players:
            player.round_score = 0
            player.round_score = player.simulate_shoot()
        return players

              