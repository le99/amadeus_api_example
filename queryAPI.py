import requests

# https://developers.amadeus.com/self-service/category/air/api-doc/airport-nearest-relevant/api-reference

access_token = "" #TODO
headers = {"Authorization": "Bearer " + access_token}
params = {
  "latitude": 51,
  "longitude": 0.4,
  "radius": 500
}

r = requests.get('https://test.api.amadeus.com/v1/reference-data/locations/airports', headers=headers, params=params)

print(r.text)     #Solo para imprimir
# print(r.json()) #Para procesar