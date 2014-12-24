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
				for i in scheme:
					print i
				print
	
	dfs(0, [])
