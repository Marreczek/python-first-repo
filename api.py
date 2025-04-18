import requests

# API_KEY = "2572|wfeAoMVTqWqW63bfovfm0UNF4oYIMmKph1QYCMR6"
#
# def get_Country():
#     URL = "https://restfulcountries.com/api/v1/countries/Nigeria"
#     req_headers = {
#         "Accept":"application/json",
#         "Authorization": f"Bearer {API_KEY}"
#     }
#     response = requests.get(url=URL, headers=req_headers)
#     country = response.json()
#     print(country["data"]["name"])
#     print(country["data"]["full_name"])
#     print(country["data"]["current_president"]["name"])
#     print(country["data"]["current_president"]["href"]["picture"])
#     print(country["data"]["description"])
#     print(country["data"]["href"]["flag"])
#
# get_Country()


API_KEY = "2572|wfeAoMVTqWqW63bfovfm0UNF4oYIMmKph1QYCMR6"

def get_Country(name):
    URL = f"https://restfulcountries.com/api/v1/countries/{name}"
    req_headers = {
        "Accept":"application/json",
        "Authorization": f"Bearer {API_KEY}"
    }
    response = requests.get(url=URL, headers=req_headers)
    country = response.json()
    print(country["data"]["name"])

get_Country("Poland")