from uwapi	import course_schedule
from date	import Date, get_first_day, get_last_day
from event	import Event
from copy	import deepcopy

def course_scheme(term, subject, catalog):
	schedule = course_schedule(term, subject, catalog)

	schemes = []
	def dfs(d, scheme):
		if(d < 4):
			if(len(schedule[d]) == 0):
				dfs(d + 1, scheme)
			for i in schedule[d]:
				tmp = scheme[:]
				tmp.append(i)
				dfs(d + 1, tmp)
		else:
			related_req = True
			for i in scheme:
				for related in i[1]:
					if(related):
						meet_req = False
						for j in scheme:
							if(related == j[0][4:]):
								meet_req = True
						if(not meet_req):
							related_req = False
			if(related_req):
				schemes.append(scheme)
	
	dfs(0, [])
	return schemes

def expand(term, scheme):
	events = []
	firstday = get_first_day(term)
	lastday = get_last_day(term)
	today = firstday

	while(today <= lastday):
		for event in scheme:
			for weekly in event[2]:
				for i in weekly[0]:
					start = Date(today.year, today.month, today.day, weekly[1], weekly[2])
					end = Date(today.year, today.month, today.day, weekly[3], weekly[4])
					start.add_day(i)
					end.add_day(i)
					events.append(Event(event[0], start, end, weekly[5]))
		today.add_day(7)
	for event in scheme:
		for onetime in event[3]:
			events.append(deepcopy(onetime))
	events.sort()

	return events

schemes = course_scheme(1151, "MATH", 136)
events = expand(1151, schemes[0])
for i in events:
	i.debug()
