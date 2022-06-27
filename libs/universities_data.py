import random
from urllib.request import urlopen
import json

class university_class:
    def university_generator(self):
        uni_object = urlopen("https://raw.githubusercontent.com/Hipo/university-domains-list/master/world_universities_and_domains.json")
        json_uni = json.loads(uni_object)
        index = random.randint(0,1000)
        name_uni = json_uni[0][index][1]
        return name_uni