file=open("New.txt","r")
import json
d={}
a=open("New.txt","r")
myfile=a.read()
a.close()
b=myfile.split()
d[b[1]]=b[2]
d[b[3]]=b[4],b[5],b[6]
d[b[7]]=b[8]
d[b[9]]=b[10]
print(d)
with open("file.json","w") as saral:
    json.dump(d,saral,indent=4)


    