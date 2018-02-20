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
	bRooms = []
	def __init__(self, id, name):
		self.bID = id
		self.bName = name

	def addRoom(self, room):
		print room
		self.bRooms += [room]
		return True

	def removeRoom(self, room):
		rIndex = self.findRoom(room)
		if rIndex == -1: # room does not exist
			return False
		self.bRooms.remove(rIndex)
		return True


	def findRoom(self, room):
		for i in range(len(self.bRooms)):
			if self.bRooms[i] == room:
				return i
		return -1

	def __str__(self):
		return self.bID + ", " + self.bName + "\nRooms: " + str(self.bRooms)

b = Building("HH", "Hamilton Hall")
b.addRoom("HH 109")
b.addRoom("HH 107")
print(b.findRoom("HH 108"))
b.removeRoom("HH 107")
print b