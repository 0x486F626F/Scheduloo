from section	import Section
from event		import Event
from date		import Date

class Course(object):
	def __init__(self, subject, sections, firstday, lastday):
		self.subject = subject
		self.sections = []
		num = 0
		for s in sections:
			num += 1
			weekly = []
			for w in s[0]:
				for d in w[0]:
					weekly.append([d, Event(Date(0, 0, 0, w[1][0], w[1][1]),
						Date(0, 0, 0, w[2][0], w[2][1]), w[3], w[4])])
			self.sections.append(Section("%03d" % (num), weekly, s[1], firstday, lastday))

	def print(self):
		print(self.subject)
		for s in self.sections:
			s.print()
