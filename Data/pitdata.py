from .masterdata import MasterData as master
import csv


class PitData:

    @staticmethod
    def import_raw_pit_data(filelocation):
        with open(filelocation, newline='') as csvfile:
            master.pitlist.clear()
            scoutingreader = csv.DictReader(csvfile, delimiter=',', quotechar='|')
            for row in scoutingreader:
                master.pitlist.append(PitData(row))

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
