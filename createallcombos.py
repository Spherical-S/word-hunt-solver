import json

letters = "abcdefghijklmnopqrstuvwxyz"
current = ""
obj = {}
temp = {}

f = open("resources\\allwords.json", "r")
allwords = json.load(f)
f.close()

for i in allwords:
    if i[0:1] not in temp:
        temp[i[0:1]] = {}
    for j in range(len(i)):
        temp[i[0:1]][i[0:j+1]] = 1

f = open("resources\\allcombos.json", "w")
json.dump(temp, f)
f.close()

print(temp["a"])


# for i in range(len(letters)):
#     current = letters[i:i+1]
#
#     f = open("resources\\"+current+".json", "r")
#     temp = json.load(f)
#     f.close()
#
#     obj[current] = temp
#
# f = open("resources\\allcombos.json", "w")
# json.dump(obj, f)
# f.close()
#
# print("done")