import csv


class MasterData:
    matchrecordlist = list() #Class variable
    pitlist = list() #Class variable

    @staticmethod
    def import_raw_match_data(filelocation):
        with open(filelocation, newline='') as csvfile:
            scoutingreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in scoutingreader:
                MasterData.matchrecordlist.append(Record(row))

    @staticmethod
    def import_raw_pit_data(filelocation):
        PitData.import_raw_pit_data(filelocation)

    @staticmethod
    def clear_data():
        MasterData.matchrecordlist.clear()

    @staticmethod
    def get_matches_by_team(teamnum):
        temp = list()
        for r in MasterData.matchrecordlist:
            if r.team == teamnum:
                temp.append(r)
        return temp

class Team:
    def __init__(self, teamnum):
        self.number = int(teamnum)
        self.update_matches()

    def update_data(self):
        self.matchlist = MasterData.get_matches_by_team(self.number)

class PitData:

    @staticmethod
    def import_raw_pit_data(filelocation):
        with open(filelocation, newline='') as csvfile:
            MasterData.pitlist.clear()
            scoutingreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in scoutingreader:
                MasterData.pitlist.append(PitData(row))

    def __init__(self, data):
        self.data = data
        self.from_dict()

    def from_dict(self):
        self.teamnum = self.data.get('Team')
        self.drivetrain = self.data.get('Drive Train')
        self.wheeltype = self.data.get('Wheel')
        self.drivetrain_motors = self.data.get('Drive Train Motors')
        self.programming_language = self.data.get('Programming Language')
        self.weight = self.data.get('Weight')
        self.hatch_scoring = self.data.get('Hatch Scoring Location')
        self.hatch_floor_pickup = self.data.get('Hatch Floor Pick Up')
        self.climbing = self.data.get('Climbing')
        self.sandstorm_positions = self.data.get('Sandstorm Positions')
        self.sandstorm_positions = self.data.get('Sandstorm Abilities')
        self.unreliable_source = self.data.get('Unreliable Source')
        self.comments = self.data.get('Comments')


class Record:
    def __init__(self, data):
        self.data = data
        self.from_dict()

    def from_dict(self):
        self.scout = self.data.get('Scout')
        self.replay = self.data.get('Replay?')
        self.team = int(self.data.get('Team'))
        self.alliance = self.data.get('Alliance')
        self.start_position = int(self.data.get('Start Position'))
        self.preload_item = int(self.data.get('Preload Item'))
        self.crossed_hab_line = bool(self.data.get('Crossed HAB Line'))
        
        self.ss_cargo_to_cs = int(self.data.get('SS Cargo to CS'))
        self.ss_cargo_to_rs_low = int(self.data.get('SS Cargo to RS Low'))
        self.ss_cargo_to_rs_mid = int(self.data.get('SS Cargo to RS Mid'))
        self.ss_cargo_to_rs_high = int(self.data.get('SS Cargo to RS Hi'))
        self.ss_cargo_drops = int(self.data.get('SS Cargo Drops'))
        self.ss_hatch_to_cs = int(self.data.get('SS Hatch to CS'))
        self.ss_hatch_to_rs_low = int(self.data.get('SS Hatch to RS Low'))
        self.ss_hatch_to_rs_mid = int(self.data.get('SS Hatch to RS Mid'))
        self.ss_hatch_to_rs_high = int(self.data.get('SS Hatch to RS Hi'))
        self.ss_hatch_drops = int(self.data.get('SS Hatch Drops'))

        self.teleop_cargo_to_cs = int(self.data.get('Teleop Cargo to CS'))
        self.teleop_cargo_to_rs_low = int(self.data.get('Teleop Cargo to RS Low'))
        self.teleop_cargo_to_rs_mid = int(self.data.get('Teleop Cargo to RS Mid'))
        self.teleop_cargo_to_rs_high = int(self.data.get('Teleop Cargo to RS Hi'))
        self.teleop_cargo_drops = int(self.data.get('Teleop Cargo Drops'))
        self.teleop_hatch_to_cs = int(self.data.get('Teleop Hatch to CS'))
        self.teleop_hatch_to_rs_low = int(self.data.get('Teleop Hatch to RS Low'))
        self.teleop_hatch_to_rs_mid = int(self.data.get('Teleop Cargo to RS Mid'))
        self.teleop_hatch_to_rs_high = int(self.data.get('Teleop Hatch to RS Hi'))
        self.teleop_hatch_drops = int(self.data.get('Teleop Hatch Drops'))
        
        self.hab_level_achieved = int(self.data.get('HAB Level Achieved'))
        self.was_assisted_climbing = bool(self.data.get('Had Assistance Climbing?'))
        self.assisted_others_climbing = bool(self.data.get('Assisted Others Climbing?'))

        self.comments = self.data.get('Comments')

        self.teleop_cargo_scored = self.teleop_cargo_to_cs + self.teleop_cargo_to_rs_low + self.teleop_cargo_to_rs_mid + self.teleop_cargo_to_rs_high
        self.teleop_hatch_scored = self.teleop_hatch_to_cs + self.teleop_hatch_to_rs_low + self.teleop_hatch_to_rs_mid + self.teleop_hatch_to_rs_high
        self.teleop_game_pieces_scored = self.teleop_cargo_scored + self.teleop_hatch_scored
        #self.match_coordinate
