#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.


from flight_search import *
from data_manager import *
from notification_manager import *

dm = DataManager()
dm.get_IATA_codes()
dm.IATA_to_sheets()

fs = FlightSearch(dm.IATA_codes)
fs.search_flights()

#dm.prices_to_sheets(fs.lowest_offers)

nm = NotificationManager(iata_codes=dm.IATA_codes, flight_details=fs.lowest_offers_complete)
nm.send_infos()
