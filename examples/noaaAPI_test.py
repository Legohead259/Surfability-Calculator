import requests
import json
import secrets
import datetime
import math

OPTIMAL_HOUR = 10
OUTGOING_PENALTY = 0.25

noaa_tidesandcurrents_http = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
response = requests.get(noaa_tidesandcurrents_http, params=secrets.noaa_parameters)
json_response = response.json()
text = json.dumps(json_response, sort_keys=True, indent=4)
# print(text)  # Debug

for datum in json_response["predictions"]:
    if datum["type"] == "L":  # Check for LOW tide only
        datetime_struct = datetime.datetime.strptime(datum["t"], "%Y-%m-%d %H:%M")  # Construct a date-time structure from the NOAA string
        hour = datetime_struct.hour
        # print(datetime_struct.hour)  # Debug

        if hour in range(7, 12):  # Only use data between 0700 and 1200
            score = 0.5*math.cos(math.pi/12*(hour-OPTIMAL_HOUR))+0.5  # Score the tide based on a cosine curve with 1 being the highest at the OPTIMAL_HOUR
            if (hour > OPTIMAL_HOUR):  # Apply outgoing tide penalty
                if score-OUTGOING_PENALTY < 0:
                    score = 0
                else:
                    score = score - OUTGOING_PENALTY
            score *= 100
            print(datum["t"], "- %d" % score, "%")  # Debug