import json
data={
    '4': 5, 
    '6': 7, 
    '1': 3, 
    '2': 4
    }

file=open("key.json","w")
json.dump(data,file,indent=4,sort_keys=True)
print(file)
file.close()