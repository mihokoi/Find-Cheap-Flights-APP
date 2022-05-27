import requests

SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/de44a0c1003a710996ebc40b71bfb2fc/flightDeals/prices"
TOKEN = "asddsaad2132313213#@Y&*#!#@!VBUJBVUDSABH"
header = {
    "Authorization": f"Bearer {TOKEN}"
}

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=header)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data
            )
            print(response.text)
