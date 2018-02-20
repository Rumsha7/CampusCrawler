## schedule data structure

from room import *

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