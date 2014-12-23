from uwaterlooapi	import UWaterlooAPI
from date			import Date
from event			import Event
uw = UWaterlooAPI(api_key="123afda14d0a233ecb585591a95e0339")
firstday = Date(2015, 1, 5, 0, 0)
lastday = Date(2015, 4, 6, 0, 0)

def course(term, subject, catalog):
	s = uw.term_course_schedule(term, subject, catalog)
	print term, subject, catalog
	for i in s:
		print i['section']
		for j in i['classes']:
			if(j['date']['end_date']):
				print j['date']['end_date'], j['date']['start_time'], j['date']['end_time']
			else:
				print j['date']['weekdays'], j['date']['start_time'], j['date']['end_time']



def course_schedule(term, subject, catalog):
	course = uw.term_course_schedule(term, subject, catalog)
	lec = []
	lab = []
	tut = []
	tst = []
	for section in course:
		desc = str(section['section'])
		related = [section['related_component_1'], section['related_component_2']]
		for i in range(2):
			if(related[i] and len(str(related[i])) == 3):
				related[i] = str(related[i])
			else:
				related[i] = None
		weekly = []
		onetime = []
		for c in section['classes']:
			h1 = int(c['date']['start_time'][:2])
			m1 = int(c['date']['start_time'][3:])
			h2 = int(c['date']['end_time'][:2])
			m2 = int(c['date']['end_time'][3:])

			if(c['date']['end_date']):
				m = int(c['date']['end_date'][:2])
				d = int(c['date']['end_date'][3:])
				onetime.append([Event(section['section'], 
					Date(lastday.year, m, d, h1, m1),
					Date(lastday.year, m, d, h2, m2), 1)])
			else:
				w = c['date']['weekdays']
				weekdays = []
				while(len(w) > 0):
					if(len(w) > 1 and w[:2] == "Th"): 
						weekdays.append(4)
						w = w[2:]
					elif(w[:1] == "M"):
						weekdays.append(1)
						w = w[1:]
					elif(w[:1] == "T"):
						weekdays.append(2)
						w = w[1:]
					elif(w[:1] == "W"):
						weekdays.append(3)
						w = w[1:]
					elif(w[:1] == "F"):
						weekdays.append(5)
						w = w[1:]
				weekdays.sort()
				weekly.append([weekdays, h1, m1, h2, m2, 1])
		all_events = [desc, related, weekly, onetime]
		if(desc[:3] == "LEC"): lec.append(all_events)
		elif(desc[:3] == "LAB"): lab.append(all_events)
		elif(desc[:3] == "TUT"): tut.append(all_events)
		elif(desc[:3] == "TST"): tst.append(all_events)
	return [lec, lab, tut, tst]
				
	

#course_schedule(1151, "MATH", 239)
#course_schedule(1151, "GENE", 123)
#course_schedule(1151, "CS", 240)
#course_schedule(1151, "CS", 241)
