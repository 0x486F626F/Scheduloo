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
				related_sections = self.db.get_related_sections(
						self.courses[i][0], self.courses[i][1], main)
				for j in range(len(related_sections)):
					for section in related_sections[j]:
						if self.ratings[i][section] == 0:
							related_sections[j].remove(section)
				if [] not in related_sections:	
					preferred_sections.append(related_sections)
			self.preferred_sections.append(preferred_sections)
	#}}}
