import json

data = {"name" : "faizan"}

with open("E:/data.json", "w") as file:
    json.dump(data, file)

with open("E:/data.json", "r") as file:
    resp = json.load(file)
print(resp)
print(resp.get("name"))
