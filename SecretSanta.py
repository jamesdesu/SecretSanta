import json
import random

#Open the adjacent names.json file.
with open("names.json", "r") as names_file:
    #Load it into the variable data.
    data = json.load(names_file)
#Get the names from the array.
names = data["names"]
#Shuffle the array.
random.shuffle(names)

#Iterate over the array.
for i in range(len(names)):
    #The name at index i gets a gift for the name at index i+1. This guarantees fairness, no need for redraws.
    print(names[i], " gets a gift for ", names[(i + 1) % len(names)])