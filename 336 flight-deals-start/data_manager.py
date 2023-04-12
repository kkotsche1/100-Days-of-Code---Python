class DataManager:



    def __init__(self):
        self.IATA_codes = []
        self.city_list = []


    def get_IATA_codes(self):
        import requests
        #----------- Getting IATA Codes for City List ----------- #

        SHEETY_GET_API = "https://api.sheety.co/353d19f8a7f5fadb98f15932efe6c05b/flightdeals/prices"
        TEQUILA_SEARCH_API = "https://tequila-api.kiwi.com/locations/query"

        sheet_data = requests.get(url=SHEETY_GET_API)
        sheet_data = sheet_data.json()["prices"]

        for city in sheet_data:
            self.city_list.append(city["city"])

        header = {
            "apikey": "eNTA3AnP-kZvRDaFAaf6hSIL-6kK024U"
        }
        for city in self.city_list:
            IATA_get_params = {
                "term": f"{city}",
                "location_types": "city"
            }
            request = requests.get(url=TEQUILA_SEARCH_API, params=IATA_get_params, headers=header)
            print(request.status_code)
            iata_list = request.json()["locations"][0]
            self.IATA_codes.append(iata_list["code"])

    def IATA_to_sheets(self):

        import requests

        x=2
        for code in self.IATA_codes:
            SHEETY_PUT_ENDPOINT = f"https://api.sheety.co/353d19f8a7f5fadb98f15932efe6c05b/flightdeals/prices/{x}"

            parameters = {
            "price":{
                "iataCode" : code
            }
            }

            request = requests.put(url=SHEETY_PUT_ENDPOINT, json=parameters)
            print(request)
            x+=1

    def prices_to_sheets(self, price_dictionary):

        import requests
        x=2
        for code in price_dictionary:
            SHEETY_PUT_ENDPOINT = f"https://api.sheety.co/353d19f8a7f5fadb98f15932efe6c05b/flightdeals/prices/{x}"

            parameters = {
            "price":{
                "lowestPrice" : price_dictionary[code]
            }
            }

            request = requests.put(url=SHEETY_PUT_ENDPOINT, json=parameters)
            print(request.status_code)
            x+=1


