import requests
import json
import secrets

noaa_tidesandcurrents_http = "https://api.tidesandcurrents.noaa.gov/api/prod/datagetter"
response = requests.get(noaa_tidesandcurrents_http, params=)