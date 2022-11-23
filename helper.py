import os
from pprint import pprint

def generate_puzzle_data():
    data = {}
    i = 0
    
    for filename in os.listdir("assets"):
        f = os.path.join("assets", filename)
        if f.endswith(".puz"):
            with open(f, mode="r") as file:
                data[i] = {}
                
                for index, line in enumerate(file):
                    value = line.split(":")[1].strip()
                    
                    if index == 0:
                        data[i]["name"] = value
                        
                    if index == 1:
                        data[i]["number"] = int(value)
                        
                    if index == 2:
                        data[i]["size"] = int(value)
                        
                    if index == 3:
                        data[i]["thumbnail"] = value
                        data[i]["images"] = {}
                        
                    if index > 3:                                        
                        num = line[0]
                        data[i]["images"][num] = value
        i += 1
    return data