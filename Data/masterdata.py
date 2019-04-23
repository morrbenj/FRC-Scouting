import csv
from .team import Team
from .record import Record
from .match import Match
from .pitdata import PitData


class MasterData:
    matchrecordlist = list()  # Class variable, individual records (team-match)
    matchlist = list()  # Class variable
    teamlist = list()  # Class variable
    pitlist = list()  # Class variable

    @staticmethod
    def import_raw_match_data(filelocation):
        with open(filelocation, newline='') as csvfile:  # Populates the matchrecordlist
            scoutingreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in scoutingreader:
                MasterData.matchrecordlist.append(Record(row))

        for i in range(1, len(MasterData.matchrecordlist), 6):  # Populates the matchlist
            if MasterData.matchrecordlist[i].match == MasterData.matchrecordlist[i+5].match:
                MasterData.matchlist.append(Match(MasterData.matchrecordlist[i:i+5]))

        for r in MasterData.matchrecordlist:  # Populates the teamlist
            if sum(r.team == s.team for s in MasterData.teamlist) == 0:
                MasterData.teamlist.append(Team(r.team))

    @staticmethod
    def import_raw_pit_data(filelocation):  # Populates the pitlist
        PitData.import_raw_pit_data(filelocation)

    @staticmethod
    def clear_data():
        MasterData.matchrecordlist.clear()
        MasterData.matchlist.clear()

    @staticmethod
    def get_matches_by_team(teamnum):
        temp = list()
        for r in MasterData.matchrecordlist:
            if r.team == teamnum:
                temp.append(r)
        return temp
