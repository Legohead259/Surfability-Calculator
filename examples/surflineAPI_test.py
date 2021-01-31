import requests
import json
import sys
import secrets
import time

types = ["wave", "wind", "tides", "weather"]
surfline_http = "https://services.surfline.com/kbyg/spots/forecasts/"
api_type = types[0]
response = requests.get(surfline_http + api_type, params=secrets.surfline_parameters)
json_response = response.json()
text = json.dumps(json_response, sort_keys=True, indent=4)
# print(text)  # Debug

for wave_data in json_response["data"]["wave"]:
    datetime_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(wave_data["timestamp"]))
    print(datetime_str)
    print(wave_data["surf"]["optimalScore"])
# print(json_response["data"]["wave"][0]["surf"]["optimalScore"])