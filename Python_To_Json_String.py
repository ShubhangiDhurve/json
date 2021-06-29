import json
data={
    "name":"shubhu",
    "age":23,
    "education":"engineering"
}
my_data=json.dumps(data)
print(my_data)
print(type(my_data))
