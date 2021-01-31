import requests
import json
import sys
import secrets
import time

from util import calculate_tide_score

surfline_http = "https://services.surfline.com/kbyg/spots/forecasts/"
api_type = "tides"
response = requests.get(surfline_http + api_type, params=secrets.surfline_parameters)
# print(response)  # Debug
json_response = response.json()
text = json.dumps(json_response, sort_keys=True, indent=4)
# print(text)  # Debug

_low_tide_in_range = False
_last_day = None
tide_data = []

for datum in json_response["data"]["tides"]:
    datetime = time.localtime(datum["timestamp"])
    # print(time.strftime("%Y-%m-%d %H:%M:%S", datetime))  # Print date and time of reading
    # print("Height: " + str(datum["height"]) + " ft")
    # print("Type: " + datum["type"])
    # print()  # Blank line

    if datetime.tm_hour in range(7, 12)  # Only append tide data for desired period
        tide_data.append(datum["height"])

    if datetime.tm_hour in range(7, 12) and datum["type"] == 'LOW':
        _low_tide_in_range = True

    if _last_day == None:
        _last_day = datetime.tm_mday
        print(_last_day)  # Debug
    elif datetime.tm_mday != _last_day:
        _last_day = datetime.tm_mday
        print(calculate_tide_score(tide_data, _low_tide_in_range))  # Debug
        tide_data = []  # reset tide data values for next day
    
