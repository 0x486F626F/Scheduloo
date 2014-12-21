from time	import Time

class Event(object):
	def __init__(self, start, end):
		self.start = start
		self.end = end

def conflict(e1, e2):
	if(e1.start < e2.start):
		return max(0, e1.end - e2.start)
	else:
		return max(0, e2.end - e1.start)
