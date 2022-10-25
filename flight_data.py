from datetime import datetime

import requests

API_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "7NGXLV5ie1F7XXLL7QsgHTKL3yyLrjx4"


class FlightData:

    def __init__(self):
        self.data = {}




    def serachFlight(self, fly_from, fly_to):
        time1 = datetime(2022, 12, 28)
        time2 = datetime(2023, 1, 6)
        location_url = f"{API_ENDPOINT}/v2/search"
        headers = {"apikey": API_KEY, }
        params = {
            "fly_from": fly_from,
            "fly_to": fly_to,
            "date_from": time1.strftime("%d/%m/%Y"),
            "date_to": time2.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 6,
            "nights_in_dst_to": 7,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "CAD"
        }

        # response = requests.get(url=location_url, headers=headers, params=params)
        stringTemp = "https://tequila-api.kiwi.com/v2/search?fly_from=YYZ&fly_to=LIR&dateFrom=28/12/2022&dateTo=06/01/2023"
        response= requests.get(url=stringTemp,headers=headers)
        response.raise_for_status()
        # data = response.json()["data"][0]
        # print(data["local_departure"])
        # flight_data = {
        #     "price":data["price"],
        #     "origin_city":data["route"][0]["cityFrom"],
        #     "origin_airport":data["route"][0]["flyFrom"],
        #     "destination_city":data["route"][0]["cityTo"],
        #     "destination_airport":data["route"][0]["flyTo"],
        #     "link": data["deep_link"]
        # }
        # return flight_data
        print(response.json())
