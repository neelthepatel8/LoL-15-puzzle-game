import random

def generate_puzzle_data(f):
    data = {}
    data["images"] = {}
    with open(f, mode="r") as file:
        for index, line in enumerate(file):
            key = line.split(":")[0]
            value = line.split(":")[1].strip()
            if index >= 4:
                data["images"][key] = value
                continue
            data[key] = value
    return data

def shuffle_puzzle(puzzle):
    keys = list(puzzle.keys())
    random.shuffle(keys)
        
    shuffled = {}
    for key in keys:
        shuffled.update({key: puzzle[key]})
    
    return puzzle, shuffled