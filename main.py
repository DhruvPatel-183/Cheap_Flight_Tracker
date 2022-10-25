#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.

import data_manager
import flight_search as fs
from datetime import datetime, timedelta
import flight_data as fd

ORIGIN_CITY_IATA = "YYZ"
# data_manag = data_manager.DataManager()
# sheet_data = data_manag.get_info()



# for city in sheet_data:
#
#     flightName = fs.FlightSearch()
#     temp_data = flightName.search(city["city"])
#     temp_code = temp_data["locations"][0]["code"]
#
#     data_manag.put_info(temp_code,city["id"])

Flightdata = fd.FlightData()

# sheet_data = data_manag.get_info()

flight = Flightdata.serachFlight(
    ORIGIN_CITY_IATA,
    "LIR"
    )
print(flight)