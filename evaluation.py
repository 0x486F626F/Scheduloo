class GraphSolver:
	
	class Vertex: #{{{
		def __init__(self, name, value):
			self.name = name
			self.value = value;
			self.available = True;
			self.edges = []

		def add_edge(self, other):
			if other not in self.edges:
				self.edges.append(other)

		def update_neighbours(self, v):
			for each in self.edges:
				each.available = v;
	#}}}
	
	def __init__(self, max_result = 10):
		self.max_result = max_result
		self.events = []
		self.index_dict = {}

	def __search_all(self, idx, current_list, num_event):
		#if len(self.search_result) >= self.max_result: return None 
		if idx == len(self.events):
			if len(current_list) == num_event: 
				value = 0
				for each in current_list:
					value += each.value
				print value
				if value >= self.highest_value:
					self.highest_value = value
				self.search_result.append(current_list)
		else:
			event = self.events[idx]
			if event.available:
				event.update_neighbours(False)
				self.__search_all(idx + 1, current_list + [event], num_event)
				event.update_neighbours(True)
			self.__search_all(idx + 1, current_list, num_event)


	def add_event(self, name, value):
		self.index_dict[name] = len(self.events)
		self.events.append(self.Vertex(name, value))

	def add_conflict(self, name1, name2):
		if name1 not in self.index_dict or name2 not in self.index_dict:
			return None
		idx1 = self.index_dict[name1]
		idx2 = self.index_dict[name2]
		self.events[idx1].add_edge(self.events[idx2])
		self.events[idx2].add_edge(self.events[idx1])

	def search_all(self, num_event):
		self.search_result = []
		self.highest_value = 0
		self.__search_all(0, [], num_event)
		print self.highest_value, len(self.search_result)
		for each in self.search_result[0]:
			print each.name
		return self.search_result
