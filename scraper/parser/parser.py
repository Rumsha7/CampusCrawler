import json
''' Parses data from schedule into data structures '''

# read file
file_object = open("data_mcmaster", "r")

# store it in data variable
data = file_object.read()

# close file
file_object.close()

# parse json data
data_dic = json.loads(data)

'''
Keys in data_dic: courses (dict), departments (dict) and last_update (string)
Courses: key - course code, value - list
times in core, lab, tutorial keys
'''

# parse through data_dic to extract all room booking times
bookingTimes = []

for i in data_dic["courses"]:
	for j in data_dic["courses"][i]:
		if "core" in str(j):
			for k in j["core"]:
				bookingTimes += k["times"]
		elif "lab" in str(j):
			for k in j["lab"]:
				bookingTimes += k["times"]
		elif "tutorial" in str(j):
			for k in j["tutorial"]:
				bookingTimes += k["times"]


# remove all elements where the room or times is TBA
bookingTimes = list(filter(lambda a: 'TBA' not in str(a), bookingTimes))

# remove all elements where the room is Online CLass, See Class Notes or CONESTOGA CAMPUS
bookingTimes = list(filter(lambda a: 'online' not in str(a).lower(), bookingTimes))
bookingTimes = list(filter(lambda a: 'conestoga' not in str(a).lower(), bookingTimes))
bookingTimes = list(filter(lambda a: 'notes' not in str(a).lower(), bookingTimes))

for i in bookingTimes:
	print i

print("Finished")