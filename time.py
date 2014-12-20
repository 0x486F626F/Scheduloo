class Time(object):
	def __init__(self, date, hour, minute):
		self.date = date
		self.hour = hour
		self.minute = minute

	def __lt__(self. other):
		if(self.date != other.date):
			return self.date < other.date
		elif(self.hour != other.hour):
			return self.hour < other.hour
		else:
			return self.minute < other.minute
