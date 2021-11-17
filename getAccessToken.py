# https://docs.python-requests.org/en/latest/
import requests

# https://developers.amadeus.com/self-service/apis-docs/guides/authorization-262

url="https://test.api.amadeus.com/v1/security/oauth2/token"
headers = {"Content-Type": "application/x-www-form-urlencoded"}
data ={
  "grant_type": "client_credentials", 
  "client_id": "",                  #API KEY, TODO
  "client_secret": ""               #API Secret, TODO
}

r = requests.post('https://test.api.amadeus.com/v1/security/oauth2/token', headers=headers, data=data)

print("access_token:")
print(r.json()["access_token"])