
import json

# first, get the absolute path to json file
PATH_TO_JSON = 'final-catalog.json' #  assuming same directory (but you can work your magic here with os.)

# read existing json to memory. you do this to preserve whatever existing data.
with open(PATH_TO_JSON,'r') as jsonfile:
    json_content = json.load(jsonfile)

with open(PATH_TO_JSON,'w') as jsonfile:
    json.dump(json_content, jsonfile, indent=1)
