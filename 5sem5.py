'''class Graph:
	def __init__(self, list_of_adjacencies):
		self.list_of_adjacencies = list_of_adjacencies

	def nodes_make(self):
		nodes = [False for u in range(len(self.list_of_adjacencies))]
		return nodes

	def dfs(self, node, list_of_nodes):
		list_of_nodes[node] = True
		print(node)
		for k in self.list_of_adjacencies[node]:
			if not list_of_nodes[k]:
				#print(k)
				l.dfs(k, list_of_nodes)
		for i in range(len(list_of_nodes)):
			if not list_of_nodes[i]:
				l.dfs(i, list_of_nodes)
		

l = Graph([[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], []])
l.dfs(0, l.nodes_make())'''

'''class Graph:
	def __init__(self, list_of_adjacencies):
		self.list_of_adjacencies = list_of_adjacencies
		self.list_of_nodes = [False for u in range(len(list_of_adjacencies))]

	def dfs(self, node):
		self.list_of_nodes[node] = True
		print(node)
		for k in self.list_of_adjacencies[node]:
			if k == len(self.list_of_nodes):
				break
			if not self.list_of_nodes[k]:
				l.dfs(k)
		for i in range(len(self.list_of_nodes)):
			if not self.list_of_nodes[i]:
				l.dfs(i)
		
	#def bfs(self, node):


l = Graph([[3], [3], [3], [0, 1, 2, 4], [3, 5], [4]])
l.dfs(0)'''

class Graph:
	def __init__(self, edges):
		self.list_of_adjacencies = []
		for i in range(len(edges) + 1):
			self.list_of_adjacencies.append([])
		self.list_of_nodes = [False for u in range(len(self.list_of_adjacencies))]
		self.list_of_levels = [-1] * len(self.list_of_adjacencies)
		print(self.list_of_levels)
		for i in range(len(edges)):
			self.list_of_adjacencies[edges[i][0]].append(edges[i][1])
			self.list_of_adjacencies[edges[i][1]].append(edges[i][0])
		print(self.list_of_adjacencies)

	def dfs(self, node):
		self.list_of_nodes[node] = True
		print(node)
		for k in self.list_of_adjacencies[node]:
			if not self.list_of_nodes[k]:
				l.dfs(k)

	def bfs(self, node):
		self.list_of_levels[node] = 0
		nodes_queue = [node]
		while nodes_queue:
			tmp_node = nodes_queue.pop(0)
			print(tmp_node)
			for i in self.list_of_adjacencies[tmp_node]:
				if self.list_of_levels[i] is -1:
					nodes_queue.append(i)
					self.list_of_levels[i] = self.list_of_levels[tmp_node] + 1

l = Graph([[0, 2], [0, 3], [1, 3], [2, 3], [2, 6], [4, 3], [5, 4]])
l.dfs(3)
print("/n")
l.bfs(3)