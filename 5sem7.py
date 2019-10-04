import numpy as np
class Network:
	def __init__(self, edges, v):
		#self.weights_dict = []
		global _infinity 
		_infinity = 10 ** 9
		a = []
		b = []
		for i in range(len(edges)):
			a.append(edges[i][0])
			b.append(edges[i][1])
		self.weights_dict = np.zeros((v+1,v+1))
		for i in range(len(edges)):
			self.weights_dict[a[i], b[i]] = int(edges[i][2])
		#print(self.weights_dict)
		self.min_path_to_i = [_infinity] * (v)
		self.used = [False] * (v)

	def min_time(self, start, v):
		self.min_path_to_i[start] = 0
		ans = 0
		p = 0
		#print(self.min_path_to_i[p])
		for i in range(v):
			min_dist = _infinity
			for j in range(v):
				#print(self.min_path_to_i[j])
				if not self.used[j] and self.min_path_to_i[j] < min_dist:
					min_dist = self.min_path_to_i[j]
					#print(min_dist)
					u = j
					#print(u, 'aa')
			ans += min_dist
			#print(min_dist)
			#print(ans)
			self.used[u] = True
			for p in range(v):
				#print(self.min_path_to_i[p])
				#print(self.weights_dict[u][p])
				if self.weights_dict[u][p] != 0.0:
					self.min_path_to_i[p] = min(self.min_path_to_i[p], self.weights_dict[u][p])
				#print(self.min_path_to_i[p])
		print(ans)
				

G = Network([[0, 3, 5], [2, 1, 11], [3, 2, 56], [1, 4, 77], [4, 5, 89]], 6)
G.min_time(0, 6)
