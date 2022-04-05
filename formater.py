# Open names.txt and format them to a yaml list called names.yml
"""import yaml


with open("names.txt", "r") as file:
    names = file.readlines()
names = [name.strip("\n") for name in names]





with open("names.yml", "w") as file:
    yaml.dump(names, file)"""
import os
import yaml
with open("names.txt", "r") as file:
    names = file.readlines()
names = [name.strip("\n") for name in names]
outputNames = []
for name in names:
    newName = name.split(" ")
    outputNames.append(newName[len(newName) - 1])


print(outputNames)

with open("names.yml", "w") as file:
    yaml.dump(outputNames, file)
