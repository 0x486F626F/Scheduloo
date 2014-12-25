class Date(object):
	def __init__(self, year, month, day, hour, minute):
		self.year = year
		self.month = month
		self.day = day
		self.hour = hour
		self.minute = minute

	def __eq__(self, other):
		return self.year == other.year\
				and self.month == other.month\
				and self.day == other.day\
				and self.hour == other.hour\
				and self.minute == other.minute

	def __ne__(self, other):
		return not(self == other)

	def __lt__(self, other):
		if(self.year != other.year):
			return self.year < other.year
		elif(self.month != other.month):
			return self.month < other.month
		elif(self.day != other.day):
			return self.day < other.day
		elif(self.hour != other.hour):
			return self.hour < other.hour
		else:
			return self.minute < other.minute

	def __le__(self, other):
		return self < other or self == other

	def __sub__(self, other):
		return self.minute - other.minute\
				+ (self.hour - other.hour) * 60\
				+ (self.day - other.day) * 24 * 60\
				+ (self.month - other.month) * days_in_month(self. year, self. month) * 24 * 60\
				+ (self.year - other.year) * (356 + is_leap(self. year)) * 24 * 60
	
	def add_day(self, d):
		self.day += d
		if(self.day > days_in_month(self.year, self.month)):
			self.day = 1
			self.month += 1
		if(self.month > 12):
			self.month = 1
			self.year += 1

	def printall(self):
		print "%d-%02d-%02d %02d:%02d" % (self.year, self.month, self.day, self.hour, self.minute)

def days_in_month(year, month):
	if(month == 2): 
		return 28 + is_leap(year)
	elif(month in [4, 6, 9, 11]):
		return 30
	else:
		return 31

def is_leap(year):
	if(year % 400 == 0):
		return 1
	elif(year % 100 == 0):
		return 0
	elif(year % 4 == 0):
		return 1
	else:
		return 0

def get_first_day(term):
	if(term == 1151):
		return Date(2015, 1, 5, 0, 0)

def get_last_day(term):
	if(term == 1151):
		return Date(2015, 4, 6, 0, 0)
