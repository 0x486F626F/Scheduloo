from event	import Event
from date	import Date

class Section(object):
#weekly = [firstday, lastday, [[desc, [1, 2, ...], h, m, h, m, v], [Event2], ...]]
	def __init__(self, subject, weekly, onetime):
		self.subject = subject
		self.events = []
		while(today <= weekly[1]):
			for event in weekly[2]:
				desc = event[0]
				for day in event[1]:
					date = today
					date.add_day(day - 1)
					self.events.append(Eveunt(desc, 
						Date(date.year, date.month, date.day, event[2], event[3]),
						Date(date.year, date.month, date.day, event[4], event[5]), event[6]))
			today.add_day(7)
		for event in onetime:
			self.events.append(event)
		self.events.sort()

	def __lt__(self, other):
		return self.subject < other.subject

	def debug(self):
		print subject
		for event in self.events:
			event.debug()
