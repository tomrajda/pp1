# 12.	Create a dictionary that describes your favourite book or film with at 
# least five key-value pairs. Then create a program that writes the dictionary 
# data to the favourite.json file. Use the dump() method. Note the formatting 
# of the data in the json file. Use the 'indent' parameter in the dump() method.

import json

film = {
    "title": "django",
    "genre": "western",
    "production": "USA",
    "world premiere": 2012,
    "polish premiere": 2013, 
}

with open('file.json', 'w') as file:
    json.dump(film, file, indent=4)