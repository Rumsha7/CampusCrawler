## schedule data structure

from room import *

class Schedule(object):
	"""docstring for Building"""
	sSchedule = {1: [], 2: [], 3: [], 4: [], 5: []} #dictionary
	sRoom = None ##Building
	def __init__(self, room):
		self.sRoom = room
		for i in range(28):
			self.sSchedule[1].append(0)
			self.sSchedule[2].append(0)
			self.sSchedule[3].append(0)
			self.sSchedule[4].append(0)
			self.sSchedule[5].append(0)

	# day, start: int
	def addTime(self, day, start):
		if not (1 <= day <= 5):
			return False
		self.sSchedule[day][self.__timeToIndex__(start)] = 1

	# convert 830 to 850 and then convert to index
	def __timeToIndex__(self, start):
		if ("30" == str(start)[-2:]):
			start = eval(str(start)[:-2] + "50")
		index = (start - 850.0) / 100 * 2
		return int(index)

	def removeTime(self, day, start):
		if not (1 <= day <= 5):
			return False
		self.sSchedule[day][self.__timeToIndex__(start)] = 0
		return True

	def checkTime(self, day, start):
		if self.sSchedule[day][self.__timeToIndex__(start)] == 0:
			return True
		return False

	def __str__(self):
		return str(self.sRoom) + ", " + str(self.sSchedule)

b = Building("HH", "Hamilton Hall")
rOne = Room("HH 109", b)
rTwo = Room("HH 107", b)
s = Schedule(rOne)
s.addTime(5, 830)
s.addTime(5, 930)
s.addTime(5, 1030)
s.addTime(5, 1130)
print s.removeTime(5, 1130)
print "\n"
print s
b.addRoom(rOne)
b.addRoom(rTwo)
print(b.findRoom(rOne))
b.removeRoom(rOne)
print "Building", b
print "Room", rOne, rTwo