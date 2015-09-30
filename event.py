import datetime

class event:
	def __init__(self, date, start_time, end_time):
		self.date = date
		self.start_time = datetime.datetime.combine(date, start_time)
		self.end_time = datetime.datetime.combine(date, end_time)
	
def conflicting_time(event1, event2):
	if (event1.start_time < event2.start_time):
		return max(datetime.timedelta(minutes = 0), 
				event1.end_time - event2.start_time)
	else:
		return max(datetime.timedelta(minutes = 0), 
				event2.end_time - event1.start_time)
