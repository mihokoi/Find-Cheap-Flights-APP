#This file will need to use the DataManager,FlightSearch, FlightData, NotificationManager classes to achieve the program requirements.
from data_manager import DataManager
from datetime import datetime, timedelta
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
notification_manager = NotificationManager()
flight_search = FlightSearch()

sheet_data = data_manager.get_destination_data()

ORIGIN_CITY_IATA = "WAW"

if sheet_data[0]["iataCode"] == "":
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

tomorrow = datetime.now() + timedelta(days=1)
six_month_from_today = datetime.now() + timedelta(days=(6*30))

for destination in sheet_data:
    flight = flight_search.check_flights(
        ORIGIN_CITY_IATA,
        destination["iataCode"],
        from_time=tomorrow,
        to_time=six_month_from_today
    )
    try:
        if flight.price < destination["lowestPrice"]:
            notification_manager.send_sms(
                message=f"Low price alert! Only PLN{flight.price} to fly from "
                        f"{flight.origin_city}-{flight.origin_airport} to "
                        f"{flight.destination_city}-{flight.destination_airport},"
                        f"from {flight.out_date} to {flight.return_date}"
            )
    except:
        continue