import numpy as np
class WeightGraph:
	def __init__(self, edges, v):
		#self.weights_dict = []
		a = []
		b = []
		for i in range(len(edges)):
			a.append(edges[i][0])
			b.append(edges[i][1])
		self.weights_dict = np.zeros((v+1,v+1))
		self.weights_dict[a, b] = int(edges[a][b][2])
		global _infinity 
		_infinity = 10 ** 9
		self.min_path_to_i = [_infinity] * (v+1)
		self.used = [False] * (v+1)

	def min_path(self, start, v):
		self.min_path_to_i[start] = 0
		ans = 0
		v= 1
		for i in range(len(self.used)):
			min_dist = _infinity
			for j in range(len(self.used)):
				if not self.used[j] and self.min_path_to_i[j] < min_dist:
					min_dist = self.min_path_to_i[j]
					u = j
			ans += min_dist
			self.used[u] = True
			for v in range(len(self.used)):
				self.min_path_to_i[v] = min(self.min_path_to_i[v], self.weights_dict[u][v])
		print(self.min_path_to_i)
				

G = WeightGraph([[0, 3, 5], [1, 2, 11], [2, 3, 56], [4, 3, 77], [4, 5, 89]], 6)
G.min_path(0, 6)