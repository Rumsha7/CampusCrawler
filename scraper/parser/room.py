## room rata structure
from building import *
class Room(object):
	"""docstring for Building"""
	rID = None #string
	rBuilding = None ##Building
	rSchedule = []
	def __init__(self, id, building):
		self.rID = id
		self.rBuilding = building

	def addRoom(self, room):
		self.bRooms.add(room)
		return True

	def removeRoom(self, room):
		if room in self.bRooms: # room does not exist
			return False
		self.bRooms.remove(room)
		return True


	def findRoom(self, room):
		return room in self.bRooms

	def __str__(self):
		return self.rID + ", " + str(self.rBuilding)

b = Building("HH", "Hamilton Hall")
rOne = Room("HH 109", b)
rTwo = Room("HH 107", b)
b.addRoom(rOne)
b.addRoom(rTwo)
print(b.findRoom(rOne))
b.removeRoom(rOne)
print "Building", b
print "Room", rOne, rTwo