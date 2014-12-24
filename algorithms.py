from uwapi	import course_schedule

def course_scheme(term, subject, catalog):
	schedule = course_schedule(term, subject, catalog)

	def dfs(d, scheme):
		if(d < 4):
			if(len(schedule[d]) == 0):
				dfs(d + 1, scheme)
			for i in schedule[d]:
				tmp = scheme[:]
				tmp.append(i)
				dfs(d + 1, tmp)
		else:
			for i in scheme:
				print i
			print
	
	dfs(0, [])


course_scheme(1151, "CS", 241)
