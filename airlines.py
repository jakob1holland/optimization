import requests

url = "https://iata-and-icao-codes.p.rapidapi.com/airlines"

headers = {
    'x-rapidapi-host': "iata-and-icao-codes.p.rapidapi.com",
    'x-rapidapi-key': "8d81a195c8msh80b6defa279ef3dp1bcdd8jsn8f8ff2763af6"
    }

response = requests.request("GET", url, headers=headers)

print(response.text)
