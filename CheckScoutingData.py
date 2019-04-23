from API import Requester
from Data.record import MasterData as master

master.import_raw_match_data()
master.import_raw_pit_data()

match = 0
for r in master.

