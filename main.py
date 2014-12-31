from uwapi	import course_schedule
from date	import Date, get_first_day, get_last_day
from event	import Event, conflict
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

def expand(term, subject, catalog, scheme):
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
					desc = subject + " " + str(catalog) + " " + event[0]
					if(start == lastday):
						start.printall()
						today.printall()
					if(start <= lastday):
						events.append(Event(desc, start, end, weekly[5]))
		today.add_day(7)
	for event in scheme:
		for onetime in event[3]:
			events.append(deepcopy(onetime))
	events.sort()
	return events

term = int(raw_input("Term = "))
num_courses = int(raw_input("Number of Courses = "))
schemes = []
subjects = []
for i in range(num_courses):
	ipt = raw_input("Course %d: " % (i + 1)).split()
	subjects.append([ipt[0], int(ipt[1])])
	schemes.append(course_scheme(term, subjects[i][0], subjects[i][1]))

all_schemes = []
def try_scheme(d, scheme):
	if(d < num_courses):
		for i in schemes[d]:
			next_scheme = scheme[:]
			next_scheme.append(i)
			try_scheme(d + 1, next_scheme)
	else:
		tmp = []
		for i in range(num_courses):
			tmp += expand(term, subjects[i][0], subjects[i][1], scheme[i])
		tmp.sort()
		all_schemes.append(tmp)
	
def analysis(events):
	l = len(events)
	lost = 0
	gain = 0
	for i in range(l):
		gain += events[i].value * (events[i].end - events[i].start)
	for i in range(l):
		for j in range(i + 1, l):
			c = conflict(events[i], events[j])
			if(c == 0): break
			lost += min(events[i].value, events[j].value) * c 
	return [gain - lost, lost]

try_scheme(0, [])

class Evaluation(object):
	def __init__(self, events, gain, lost):
		self.events = events
		self.gain = gain
		self.lost = lost
	def __lt__(self, other):
		if(self.lost != other.lost):
			return self.lost < other.lost
		return self.gain > other.gain

evaluations = []
for i in range(len(all_schemes)):
	print "%d/%d" % (i, len(all_schemes))
	grade = analysis(all_schemes[i])
	print grade[0], grade[1]
	evaluations.append(Evaluation(all_schemes[i], grade[0], grade[1]))

evaluations.sort()
for i in evaluations:
	if(i.lost == 0):
		print i.gain, i.lost
print

print evaluations[0].gain, evaluations[0].lost
for i in evaluations[0].events:
	i.debug()
