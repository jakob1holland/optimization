# https://rapidapi.com/Active-api/api/airport-info/

import requests

url = "https://airport-info.p.rapidapi.com/airport"

querystring = {"iata":"ord"}

headers = {
    'x-rapidapi-host': "airport-info.p.rapidapi.com",
    'x-rapidapi-key': "8d81a195c8msh80b6defa279ef3dp1bcdd8jsn8f8ff2763af6"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

print(response.text)