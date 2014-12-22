import event

from event	import Event
from date	import Date

class Section(object):
	def __init__(self, number, weekly, onetime, firstday, lastday):
		self.number = number
		self.events = []
		today = firstday
		while(today <= lastday):
			for e in weekly:
				start = Date(today.year, today.month, today.day + e[0] - 1, 
						e[1].start.hour, e[1].start.minute)
				end = Date(today.year, today.month, today.day + e[0] - 1, 
						e[1].end.hour, e[1].end.minute)
				self.events.append(Event(start, end, e[1].value, e[1].description))
			today.add_day(7)
		for e in onetime:
			self.events.append(e)
		self.events.sort()
