import requests
import json
import sys
import secrets
import time

from util import calculate_wave_score

surfline_http = "https://services.surfline.com/kbyg/spots/forecasts/"
api_type = "wave"
response = requests.get(surfline_http + api_type, params=secrets.surfline_parameters)
# print(response)  # Debug
json_response = response.json()
text = json.dumps(json_response, sort_keys=True, indent=4)
# print(text)  # Debug

for wave_data in json_response["data"]["wave"]:
    print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(wave_data["timestamp"])))  # Print date and time of reading
    print("Surfline score: " + str(wave_data["surf"]["optimalScore"]))
    print("Max surf: " + str(wave_data["surf"]["max"]) + " ft")
    print("Min surf: " + str(wave_data["surf"]["min"]) + " ft")
    print("Calculated score: " + str(calculate_wave_score(wave_data["surf"]["min"], wave_data["surf"]["max"])))
    print()  # Blank line