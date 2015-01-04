from uwaterlooapi	import UWaterlooAPI
from os.path		import isfile
uw = UWaterlooAPI(api_key="123afda14d0a233ecb585591a95e0339")
dir_path = "schedules/"

def course_schedule(term, subject, catalog):
	firstday = get_first_day(term)
	lastday = get_last_day(term)
	course = uw.term_course_schedule(term, subject, catalog)
	lec = []
	lab = []
	tut = []
	tst = []
	for section in course:
		desc = str(section['section'])
		value = raw_input("%s %s %s value = " % (subject, catalog, desc))
		value = int(value)
		if(section['campus'] == 'ONLN ONLINE'):
			continue
		related = ['00' + str(section['associated_class']), section['related_component_1'], section['related_component_2']]
		for i in range(3):
			if(related[i] and len(str(related[i])) == 3):
				related[i] = str(related[i])
			else:
				related[i] = None
		weekly = []
		onetime = []
		for c in section['classes']:
			start = [int(c['date']['start_time'][:2]), int(c['date']['start_time'][3:])]
			end = [int(c['date']['end_time'][:2]), int(c['date']['end_time'][3:])]

			if(c['date']['end_date']):
				m = int(c['date']['end_date'][:2])
				d = int(c['date']['end_date'][3:])
				onetime.append(Event(subject + " " + str(catalog) + " " + section['section'], 
					Date(lastday.year, m, d, start[0], start[1]),
					Date(lastday.year, m, d, start[0], start[1]), value))
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
				weekly.append([weekdays, start[0], start[1], end[0], end[1], value])
		all_events = [desc, related, weekly, onetime]
		if(desc[:3] == "LEC"): lec.append(all_events)
		elif(desc[:3] == "LAB"): lab.append(all_events)
		elif(desc[:3] == "TUT"): tut.append(all_events)
		elif(desc[:3] == "TST"): tst.append(all_events)
	return [lec, lab, tut, tst]

def get_schedule(term, subject, number):
	'''get the course schedule of 'subject number' in term 'term'
	example: get_schdule(1151, "CS", "241")'''
	file_path = dir_path + str(term) + "/" + subject + number
	if(isfile(file_path)):
		return get_from_file(file_path)
	else:
		return get_from_uw(term, subject, number)

