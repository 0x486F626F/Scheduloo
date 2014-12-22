from event	import Event
from date	import Date
from section	import Section

weekly = [[1, Event(Date(0, 0, 0, 11, 30), Date(0, 0, 0, 12, 20), 10, "LEC")], 
		[3, Event(Date(0, 0, 0, 11, 30), Date(0, 0, 0, 12, 20), 10, "LEC")],
		[5, Event(Date(0, 0, 0, 11, 30), Date(0, 0, 0, 12, 20), 10, "LEC")],
		[1, Event(Date(0, 0, 0, 12, 30), Date(0, 0, 0, 13, 20), 1, "TUT")]]
onetime = [Event(Date(2014, 10, 6, 19, 0), Date(2014, 10, 6, 20, 50), 100, "TST")] 
firstday = Date(2014, 9, 8, 0, 0)
lastday = Date(2014, 12, 1, 0, 0)

sec = Section("001", weekly, onetime, firstday, lastday)

print(sec.number)

for e in sec.events:
	e.print()

