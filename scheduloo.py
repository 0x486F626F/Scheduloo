import event
import datetime
import evaluation

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

	def set_ratings(self, ratings): #{{{
		self.ratings = []
		for i in range(len(self.opening_sections)):
			rating_pairs = {}
			for j in range(len(self.opening_sections[i])):
				for k in range(len(self.opening_sections[i][j])):
					rating_pairs[self.opening_sections[i][j][k]] = ratings[i][j][k]
			self.ratings.append(rating_pairs)
		
		self.preferred_sections = []
		for i in range(len(self.courses)):
			preferred_sections = []
			for main in self.opening_sections[i][0]:
				related_sections = self.db.get_related_sections(self.courses[i][0], self.courses[i][1], main)
				for j in range(len(related_sections)):
					for section in related_sections[j]:
						if self.ratings[i][section] < 0:
							related_sections[j].remove(section)
				if [] not in related_sections:	
					preferred_sections.append(related_sections)
			self.preferred_sections.append(preferred_sections)
	#}}}
	
	def make_event_list(self, start_date, end_date, time_schedule): #{{{
		study_days = []
		event_list = []
		if (time_schedule == []): return event_list
		if not (time_schedule[0] == []):
			# get weekdays that have courses
			weekly_class = time_schedule[0]
			for section in weekly_class:
				for weekdays in section[0]:
					if not weekdays in study_days:
						study_days.append(weekdays)
			study_days.sort()
			# separating the weekly class into specific date
			now = start_date
			i = 0
			while now <= end_date:
				today = now.isoweekday()
				if (today in study_days):
					for section in weekly_class:
						if (today in section[0]):
							event_list.append([now, section[1], section[2]])
					incre = 0
					if (len(study_days) > 1):
						incre = (study_days[i + 1] - study_days[i] + 7) % 7
					else: incre = 1
					now += datetime.timedelta(days = incre)
				else: now += datetime.timedelta(days = 1)
			i = (i + 1) % len(study_days)
		# adding the one-time courses
		if (len(time_schedule) > 1):
			event_list = event_list + time_schedule[1]
		event_list.sort()
		return event_list
	# }}}

	def make_combination(self, current, idx, lists): #{{{
		if idx == len(lists):
			self.combination.append(current)
		else:
			for component in lists[idx]:
				self.make_combination(current + [component], idx + 1, lists)
		#}}}
	
	def evaluate_all_combinations(self):
		all_combinations = []
		for course in self.preferred_sections:
			course_combinations = []
			for section in course:
				self.combination = []
				self.make_combination([], 0, section)
				course_combinations += self.combination
			all_combinations.append(course_combinations)
		self.combination = []
		self.make_combination([], 0, all_combinations)
		all_combinations = self.combination
		
		for combination in all_combinations:
			for i in range(len(self.courses)):
				for section in combination[i]:
					print self.courses[i][0], self.courses[i][1], section
					time_schedule = self.db.get_time_schedule(
							self.courses[i][0],
							self.courses[i][1],
							section)
					print evaluation.evaluate(self.make_event_list(
							datetime.date(2015, 9, 14),
							datetime.date(2015, 12, 4),
							time_schedule))
