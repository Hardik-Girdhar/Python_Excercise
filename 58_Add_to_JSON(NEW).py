import json
with open("json.txt","r+") as file:
    d = json.loads(file.read())
    d["employees"].append(dict(firstName="Hardik", lastName= "Girdhar"))
    file.seek(0)
    json.dump(d, file, indent =4, sort_keys = True)
    file.truncate()
