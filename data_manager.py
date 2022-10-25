import requests
from pprint import pprint



class DataManager:
    def __init__(self):
        self.data = {}
    def get_info(self):
        response = requests.get("https://api.sheety.co/f6103ae815982a4834e3c4cb76e0cff9/flightDeals/prices")
        self.data= response.json()["prices"]
        return self.data


    def put_info(self,code,id):
        temp_data = {
            "price": {
                "iataCode": code
            }
        }
        response = requests.put(f"https://api.sheety.co/f6103ae815982a4834e3c4cb76e0cff9/flightDeals/prices/{id}",json=temp_data)
        # print(response.text)