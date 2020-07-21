import requests
from Models.single_postcode_model import PostCode
from config_manager import base_url


# This model processes the data, i.e. retrieves all the information from API
class SinglePC():

    def __init__(self, single_postcode):
        self.url = base_url() + single_postcode
        self.request = requests.get(self.url)
        self.header_details = self.request.headers
        self.response_json = self.request.json()

    def response(self):
        return PostCode(self.response_json)


pc = SinglePC("B7 4BB")
print(pc.response().latitude)

# Its fine to have objects stored as a list
# Python cannot dynamically assign variables

# Work on postcode class
# Link to other APIs and build something from it
# 1. Generate info on a random user (look at documentation to tell you how to use it)
# 2. Big database of TV shows (query by name)
# 3. Pokemon API (reccomended)
    # Some details are linked to other APIs
    # when you get a response that is a URL, sent out another request to retrieve information

# Think about a few tests, read documentation, think about a config manager
# Find some that require API keys, if possible
