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
