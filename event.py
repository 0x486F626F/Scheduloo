import datetime

class onetime_event:
	def __init__(self, date, start_time, end_time):
		self.date = date
		self.start_time = start_time
		self.end_time = end_time

class weekly_event:
	def __init__(self, weekdays, start_time, end_time):
		self.weekdays = weekdays
		self.start_time = start_time
		self.end_time = end_time

def time_conflict(event1, event2):
	today = datetime.date.today()
	combine = datetime.datetime.combine
	zero = datetime.timedelta(seconds = 0)

	start_time1 = combine(today, event1.start_time)
	end_time1 = combine(today, event1.end_time)
	start_time2 = combine(today, event2.start_time)
	end_time2 = combine(today, event2.end_time)
	if (start_time1 < start_time2):
		return max(zero, end_time1 - start_time2) / 60
	else:
		return max(zero, end_time2 - start_time1) / 60
