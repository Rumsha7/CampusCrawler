## schedule data structure

from room import *

class Schedule(object):
	"""docstring for Building"""
	sSchedule = {1: [], 2: [], 3: [], 4: [], 5: []} #dictionary
	sRoom = None ##Building
	def __init__(self, room):
		self.sRoom = room
		for i in range(28):
			self.sSchedule[1].append("")
			self.sSchedule[2].append("")
			self.sSchedule[3].append("")
			self.sSchedule[4].append("")
			self.sSchedule[5].append("")

	def addTime(self, time):
		return False

	def removeTime(self, time):
		return False

	def checkTime(self, time):
		return False

	def __str__(self):
		return self.sRoom + ", " + str(self.sSchedule)