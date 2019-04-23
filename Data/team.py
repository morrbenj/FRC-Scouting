from .masterdata import MasterData

class Team:
    def __init__(self, teamnum):
        self.number = int(teamnum)
        self.update_data()

    def update_data(self):
        self.matchlist = MasterData.get_matches_by_team(self.number)
