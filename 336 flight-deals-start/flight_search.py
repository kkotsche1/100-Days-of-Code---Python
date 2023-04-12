class FlightSearch:
    #This class is responsible for talking to the Flight Search API.

    def __init__(self, IATA_codes):
        self.IATA_codes = IATA_codes
        self.lowest_offers_complete = {}
        self.lowest_offers = {}
        self.todays_date = None
        self.last_outbound = None


    def search_flights(self):
        from datetime import datetime, timedelta
        import requests

        now = datetime.today()
        self.todays_date = now.strftime("%d/%m/%Y")
        self.last_outbound = now + timedelta(days=1)
        self.last_outbound = self.last_outbound.strftime("%d/%m/%Y")

        #----------- Accessing Flight Search --------- #

        for IATA_code in self.IATA_codes:
            HEADER = {
                "apikey": "eNTA3AnP-kZvRDaFAaf6hSIL-6kK024U"
            }
            FLIGHT_SEARCH_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"

            flight_search_data = {
                "fly_from": f"airport:CGN",
                "fly_to": f"city:{IATA_code}",
                "date_from": self.todays_date,
                "date_to": self.last_outbound,
                "nights_in_dst_from": 5,
                "nights_in_dst_to": 5,
                "flight_type": "round",
                "adults": 1,
                "selected_cabins": "M"

            }
            request = requests.get(url=FLIGHT_SEARCH_ENDPOINT, params=flight_search_data, headers=HEADER)
            data = request.json()["data"]
            self.lowest_offers_complete[f"{IATA_code}"] = data[0]
            self.lowest_offers[f"{IATA_code}"] = data[0]["price"]

            print(self.lowest_offers_complete[IATA_code])


