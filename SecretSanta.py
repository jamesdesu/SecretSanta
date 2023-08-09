import json
import random
with open("names.json", "r") as names_file:
    data = json.load(names_file)
names = data["names"]
random.shuffle(names)

for i in range(len(names)):
    print(names[i], " gets a gift for ", names[(i + 1)%len(names)])