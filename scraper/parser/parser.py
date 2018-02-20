import json
''' Parses data from schedule into data structures '''

# read file
file_object = open("data_mcmaster", "r")

# store it in data variable
data = file_object.read()

# parse json data
data_dic = json.loads(data)

courses = data_dic["courses"]
philos = courses["PHILOS"]
name = philos[0]["name"]

print(name)

file_object.close()

print("Finished")
