from date	import Date

class Event(object):
	def __init__(self, start, end, value):
		self.start = start
		self.end = end
		self.duration = end - start
		self.value = value
	def print(self):
		self.start.print()

def conflict(e1, e2):
	if(e1.start < e2.start):
		return max(0, e1.end - e2.start)
	else:
		return max(0, e2.end - e1.start)

