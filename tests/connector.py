import json
from urllib.request import urlopen


class Connector:
    base_url = "https://beyondaporia.com/sonnets/"

    def __init__(self):
        pass

    def get_all(self):
        response = urlopen(self.base_url + "all").read().decode('UTF-8')
        return json.loads(response)

    def get_author_last_name(self, last_name):
        response = urlopen(self.base_url + "by_author_last_name/" + last_name) \
            .read().decode('UTF-8')
        return json.loads(response)
