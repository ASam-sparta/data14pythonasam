import requests
import json
from pprint import pprint

# dict_body = {'postcodes': ["B7 4BB", "OX49 5NU", "M32 0JG", "NE30 1DP"] }
# json_body = json.dumps(dict_body)
# headers = {'Content-Type': 'application/json'}
#
# address = "https://api.postcodes.io/postcodes/"
# req_response = requests.post(address, headers=headers, data=json_body)
#
# results = req_response.json()['result']
# pprint(results)
#
# for i in range(len(results)):
#     postcode = results[i]['result']['postcode']
#     eastings = results[i]['result']['eastings']
#     northings = results[i]['result']['northings']
#     NUTS_code = results[i]['result']['codes']['nuts']
#     print(f"Postcode is {postcode}, Eastings = {eastings}, Northings = {northings}, NUTS code = {NUTS_code}")

# Print the postcode, eastings northings and NUTS code for each result


address = "https://api.postcodes.io/postcodes/B7 4BB"
req_response = requests.get(address)

# print(req_response)
# print(type(req_response))
#
# # HTTP Status Code
# # 404 - Page Not Found
# # 200 - OK
#
# print(req_response.status_code)
# pprint(req_response.json())  # This is a byte string, turns into python dict
# result = req_response.json()["result"]
# print(f"{result['eastings']}, {result['northings']}")
# print(f"The nuts code is {result['codes']['nuts']}")


# Think about how a class can be constructed
# Postcode is object, attributes are others

class Postcode:
    def __init__(self, postcode):
        self.postcode = postcode
        self.nuts_code()
        self.eastings()
        self.northings()
        # self.get_data()

    # def get_data(self):
    #     address = f"https://api.postcodes.io/postcodes/{self.postcode}"
    #     req_response = requests.get(address)
    #     return req_response

    def nuts_code(self):
        address = f"https://api.postcodes.io/postcodes/{self.postcode}"
        req_response = requests.get(address)
        if req_response.status_code == 200:
            return req_response.json()['result']['codes']['nuts']
        elif req_response.status_code == 404:
            return "Please enter a valid postcode"

    def eastings(self):
        address = f"https://api.postcodes.io/postcodes/{self.postcode}"
        req_response = requests.get(address).json()
        return req_response['result']['eastings']

    def northings(self):
        address = f"https://api.postcodes.io/postcodes/{self.postcode}"
        req_response = requests.get(address).json()
        return req_response['result']['northings']

my_house = Postcode("B7 4BB")
pprint(my_house.nuts_code())
pprint(my_house.eastings())
pprint(my_house.northings())

# THink about how class behaves under different response circumstances 404