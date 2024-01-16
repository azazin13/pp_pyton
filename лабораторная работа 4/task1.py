import json

file1 = "input.json"

def task() -> float:
    with open(file1, "r") as f:
        data = json.load(f)
        result = 0
        for dict_ in data:
            result += dict_["score"]*dict_['weight']
        return round(result, 3)


print(task())
