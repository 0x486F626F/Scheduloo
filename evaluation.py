import datetime
import event

class tree: #{{{
	class node:
		def __init__(self, l_node = None, r_node = None, value = 0):
			self.l_node = l_node
			self.r_node = r_node
			self.m_value = None
			self.value = value
		
		def passdown(self):
			return None

	def _new_node(self):
		return None

	def __init__(self, l_key, r_key):
		self.root = self._new_node()
		self.l_key = l_key
		self.r_key = r_key

	def _cover(self, root, l_key, r_key, start, end, value):
		root.passdown()
		if l_key == start and r_key == end:
			root.value += value
			return

		if root.m_value is None:
			if start - l_key > r_key - end:
				root.m_value = start
			else:
				root.m_value = end
			root.l_node = self._new_node()
			root.r_node = self._new_node()

		mid = root.m_value
		if end <= mid:
			self._cover(root.l_node, l_key, mid, start, end, value)
		elif start >= mid:
			self._cover(root.r_node, mid, r_key, start, end, value)
		else:
			self._cover(root.l_node, l_key, mid, start, mid, value)
			self._cover(root.r_node, mid, r_key, mid, end, value)

	def _query(self, root, l_key, r_key, start, end):
		root.passdown()
		mid = root.m_value
		if mid is None:
			if root.value > 0:
				return [[start, end, root.value]]
			else:
				return []
		elif end <= mid:
			return self._query(root.l_node, l_key, mid, start, end)
		elif start >= mid:
			return self._query(root.r_node, mid, r_key, start, end)
		else:
			return self._query(root.l_node, l_key, mid, start, mid) + \
					self._query(root.r_node, mid, r_key, mid, end)

	def query(self, begin, end):
		if begin < end:
			return self._query(self.root, self.l_key, self.r_key, begin, end)
		else:
			return []
	#}}}

class cover_tree(tree): #{{{
	class node(tree.node):
		def passdown(self):
			if self.m_value is not None:
				self.l_node.value += self.value
				self.r_node.value += self.value
				self.value = 0
	
	def _new_node(self):
		return self.node()

	def cover(self, begin, end):
		if begin < end: 
			self._cover(self.root, self.l_key, self.r_key, begin, end, 1)
	#}}}

class value_tree(tree): #{{{
	class node(tree.node):
		def passdown(self):
			if self.m_value is not None:
				self.l_node.value = max(self.l_node.value, self.value)
				self.r_node.value = max(self.r_node.value, self.value)
				self.value = 0
	
	def _new_node(self):
		return self.node()

	def cover(self, begin, end, value):
		if begin < end:
			self._cover(self.root, self.l_key, self.r_key, begin, end, value)
	#}}}

def __preorder(events, values):
	if len(events) < 3:
		result = []
		for i in range(len(events)):
			result.append([events[i], values[i]])
		return result
	mid = len(events) / 2
	return [[events[mid], values[mid]]] + \
			__preorder(events[:mid], values[:mid]) + \
			__preorder(events[mid + 1:], values[mid + 1:])

def evaluate(events, values):
	l_key = sorted(events, key = lambda event: event.start_time)[0].start_time
	r_key = sorted(events, key = lambda event: event.end_time)[-1].end_time
	t_cover = cover_tree(l_key, r_key)
	t_value = value_tree(l_key, r_key)
	event_value_pairs = __preorder(events, values)
	for pair in event_value_pairs:
		t_cover.cover(pair[0].start_time, pair[0].end_time)
		t_value.cover(pair[0].start_time, pair[0].end_time, pair[1])
	events_list = [t_cover.query(l_key, r_key), t_value.query(l_key, r_key)]
	value_sum = 0
	conflicting_time = 0
	for i in range(len(events_list[0])):
		diff = (events_list[1][i][1] - events_list[1][i][0]).total_seconds()/60
		value_sum += diff * events_list[1][i][2]
		conflicting_time += diff * (events_list[0][i][2] - 1)
	return [value_sum, conflicting_time]

