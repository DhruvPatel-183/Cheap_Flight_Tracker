import requests


API_ENDPOINT = "https://tequila-api.kiwi.com"
API_KEY = "7NGXLV5ie1F7XXLL7QsgHTKL3yyLrjx4"

class FlightSearch:

    def __init__(self):
        self.data = {}
    def search(self,city_name):

        location_url = f"{API_ENDPOINT}/locations/query"
        headers = {"apikey": API_KEY,}
        params = {"term": city_name, "location_types":"city"}

        response = requests.get(url=location_url, headers=headers, params=params)
        response.raise_for_status()
        self.data = response.json()
        return self.data

