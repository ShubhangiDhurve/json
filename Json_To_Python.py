# file=open("my_file.json","w")
# json.dump(dict,file,indent=4)
# file.close()
import json
file=open("shu.json","r")
data=json.load(file)
print(data)