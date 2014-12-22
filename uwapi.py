from uwaterlooapi import UWaterlooAPI
uw = UWaterlooAPI(api_key="123afda14d0a233ecb585591a95e0339")


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

course(1151, "MATH", 136)
print
course(1151, "MATH", 138)
print
course(1151, "CS", 136)
