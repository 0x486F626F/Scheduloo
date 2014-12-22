from event	import Event
from date	import Date
from section	import Section
from course	import Course

onetime = [Event(Date(2014, 10, 6, 19, 0), Date(2014, 10, 6, 20, 50), 100, "TST 201")] 
firstday = Date(2014, 9, 8, 0, 0)
lastday = Date(2014, 12, 1, 0, 0)

s1 = [[[[1, 3, 5], [11, 30], [12, 20], 10, "LEC 001"], [[1], [12, 30], [13, 20], 1, "TUT 101"]], onetime]
s2 = [[[[1, 3, 5], [13, 30], [14, 20], 10, "LEC 002"], [[2], [16, 30], [17, 20], 1, "TUT 102"]], onetime]

c = Course("MATH 136", [s1, s2], firstday, lastday)

c.print()
