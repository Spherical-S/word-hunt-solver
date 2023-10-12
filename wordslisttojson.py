import json

f = open("scrabblewords.txt", "r")
temp = f.readlines()
f.close()

obj = {}

for i in range(len(temp)):
    obj[temp[i].lower()[:-2]] = 1

f = open("allwords.json", "w")
json.dump(obj, f)
f.close()

print("done")