import datetime
import evaluation
import event

class Scheduloo:
	def __init__(self, db):
		self.db = db

	def set_courses(self, courses): #{{{
		self.courses = courses
		self.opening_sections = []
		for course in courses:
			self.db.update_course(course[0], course[1])
			self.opening_sections.append(self.db.get_opening_sections(course[0], course[1]))
		for course in courses:
			self.db.update_course(course[0], course[1])
	#}}}

	def add_conflict(self, key1, key2):
		if key1 not in self.conflicts and key2 not in self.conflicts:
			self.conflicts[key1] = key2

	def set_solver(self, ratings): #{{{
		self.solver = evaluation.GraphSolver()
		self.total_component = 0
		all_sections = []
		self.conflicts = {}
		for i in range(len(self.opening_sections)):
			course_name = self.courses[i][0] + self.courses[i][1]
			for j in range(len(self.opening_sections[i])):
				self.total_component += 1
				length = len(self.opening_sections[i][j])
				for k in range(length):
					all_sections.append([
						self.courses[i][0], self.courses[i][1], 
						self.opening_sections[i][j][k], ratings[i][j][k]])
					for l in range(k):
						self.add_conflict(
								course_name + self.opening_sections[i][j][k],
								course_name + self.opening_sections[i][j][l])

			for main_event in self.opening_sections[i][0]:
				related_sections = self.db.get_related_sections(
						self.courses[i][0], self.courses[i][1], main_event)
				for j in range(1, len(self.opening_sections[i])):
					for section in self.opening_sections[i][j]:
						if section not in related_sections[j]:
							self.add_conflict(
									course_name + main_event,
									course_name + section)
		all_sections = sorted(all_sections, key = lambda section: - section[3])
		for section in all_sections:
			self.solver.add_event(section[0] + section[1] + section[2], section[3])
		for key in self.conflicts:
			self.solver.add_conflict(key, self.conflicts[key])
		for i in range(len(all_sections)):
			for j in range(i):
				name1 = all_sections[i][0] + \
						all_sections[i][1] + \
						all_sections[i][2]
				name2 = all_sections[j][0] + \
						all_sections[j][1] + \
						all_sections[j][2]
				schedule1 = self.get_time_schedule(
						all_sections[i][0], 
						all_sections[i][1], 
						all_sections[i][2]) 
				schedule2 = self.get_time_schedule(
						all_sections[j][0], 
						all_sections[j][1], 
						all_sections[j][2]) 
				conflict_time = event.get_total_conflict(schedule1, schedule2)
				if conflict_time > 0:
					self.solver.add_conflict(name1, name2)

	#}}}

	def get_time_schedule(self, subject, catalog, section): #{{{
		result = self.db.get_time_schedule(subject, catalog, section)
		schedule = [[], []]
		for weekly in result[0]:
			schedule[0].append(
					event.weekly_event(weekly[0], weekly[1], weekly[2]))
		for onetime in result[1]:
			schedule[1].append(
					event.onetime_event(onetime[0], onetime[1], onetime[2]))
		return schedule
	#}}}

	def search_all(self):
		print self.total_component
		result = self.solver.search_all(self.total_component)
		return result
