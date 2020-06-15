import json

test = {
    'name': 'Tim',
    'website': 'apple.com',
    'from': 'Alabama'
}

with open('data.txt', 'w') as outfile:
    json.dump(test, outfile)