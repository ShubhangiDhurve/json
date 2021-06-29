import json
file=open("New.txt","r")
data=json.load(file)
print(data)
print(type(data))
file.close()