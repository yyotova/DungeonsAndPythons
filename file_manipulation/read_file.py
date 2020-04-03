from copy import deepcopy 
import json

def read_from_file_with_first_level(file_name):
    level_array = []
    
    file = open(file_name,"r")
    content = file.readlines()
    for line in content:
        helper_list=[]
        for letter in range(0,len(line)):
            if line[letter] != "\n":
                helper_list.append(line[letter])
        level_array.append(helper_list)

    file.close()

    return level_array

def read_from_file_with_treasures(file_name):
    treasures = {
    'potion': [],
    'spell': [],
    'weapon': []
    }
    with open(file_name) as f:
        for line in f:
            treasure, description = line.strip().split(None, 1)

            treasures[treasure].append(description.strip())

    #converting to a dictionary
    for key, value in treasures.items():
        for index in range(len(value)):
            value[index] = json.loads(value[index])

    return treasures

def read_from_file_with_enemies(file_name):
    enemies = {
    'enemy': []
    }

    with open(file_name) as f:
        for line in f:
            enemies['enemy'].append(json.loads(line))

    return enemies
  