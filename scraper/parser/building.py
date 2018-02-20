## building data structure
'''
Building {
		String id //short form name
		String name
		ArrayList[Room]

}
'''
class Building(object):
	"""docstring for Building"""
	bID = None #string
	bName = None #string
	bRooms = set()
	def __init__(self, id, name):
		self.bID = id
		self.bName = name

	def addRoom(self, room):
		print room
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
		return self.bID + ", " + self.bName + "\n Rooms: " + str(self.bRooms)

#b = Building("HH", "Hamilton Hall")
#b.addRoom("HH 109")
#b.addRoom("HH 107")
#print(b.findRoom("HH 109"))
#b.removeRoom("HH 107")
#print b