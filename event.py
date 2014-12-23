from date	import Date
class Event(object):
	def __init__(self, desc, start, end, value):
		self.desc = desc
		self.start = start
		self.end = end
		self.value = value

	def __lt__(self, other):
		return self.start < other.start

	def debug(self):
		print self.desc, self.value, "%02d-%02d %02d:%02d~%02d:%02d" % \
				(self.start.month, self.start.day, 
						self.start.hour, self.start.minute, 
						self.end.hour, self.end.minute)

def conflict(e1, e2):
	if(e1.start < e2.start):
		return max(0, e1.end - e2.start)
	else:
		return max(0, e2.end - e1.start)
