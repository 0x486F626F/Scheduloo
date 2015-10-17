import sqlite3


class RatingRecords:
	

	def __init__(self, term, path = 'db/'): #{{{
		self.term = term
		self.path = path
		self.sql = sqlite3.connect(path + str(term) + 'ratingrecords.db')
		self.db= self.sql.cursor()
		command = 'CREATE TABLE IF NOT EXISTS rating_records' + \
				'''(subject			TEXT,
				    catalog_number  TEXT,
					section			TEXT,
					rating_times	REAL,
					mean			REAL);'''
		self.db.execute(command)
		self.sql.commit()
	#}}}
	
	def add_section(self, subject, catalog_number, section): #{{{
		command = '''INSERT INTO rating_records 
					(subject, catalog_number, section, rating_times, mean)
					VALUES( ''' + "'" + subject + "', " + catalog_number + \
					", '" + section + "', 0, 0);"
		self.db.execute(command)
		self.sql.commit()
	#}}}

	def update_section(self, subject, catalog_number, section ,rate): #{{{
		condition = "WHERE subject = '" + subject + "'AND " + \
						"catalog_number = '" + catalog_number + "'AND " + \
						"section = '" + section + "';"
		self.db.execute("SELECT * FROM rating_records " + condition)
		result = self.db.fetchall()
		if (result == []):
			self.add_section(subject, catalog_number, section)
			self.update_section(subject, catalog_number, section, rate)
		else:
			num_ratings = result[0][3]
			mean = result[0][4]
			mean = (mean * num_ratings + rate) / (num_ratings + 1)
			num_ratings += 1
			command = 'UPDATE rating_records SET ' + \
				'mean = ' + str(mean) + ', ' + 'rating_times = ' + \
				str(num_ratings) + ' ' + condition
			self.db.execute(command)
			self.sql.commit()
	#}}}


