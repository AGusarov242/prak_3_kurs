class WeightGraph:
    def __init__(self, edges):
        self.weights_dict = {}
        max_node = 0
        for i in range(len(edges)):
            self.weights_dict[(edges[i][0], edges[i][1])] = edges[i][2]
            if edges[i][0] > max_node or edges[i][1] > max_node:
                max_node = max(edges[i][0], edges[i][1])
        node_count = max_node + 1
        _infinity = 10 ** 9
        self.min_path_to_i = [_infinity] * node_count
        self.prev = [None] * node_count

    def min_path(self, start, finish):
        self.min_path_to_i[start] = 0
        for k in range(1, len(self.prev)):
            for j, i in self.weights_dict.keys():
                if self.min_path_to_i[j] + self.weights_dict[j, i] < self.min_path_to_i[i]:
                    self.min_path_to_i[i] = self.min_path_to_i[j] + self.weights_dict[j, i]
                    self.prev[i] = j
                if self.min_path_to_i[i] + self.weights_dict[j, i] < self.min_path_to_i[j]:
                    self.min_path_to_i[j] = self.min_path_to_i[i] + self.weights_dict[j, i]
                    self.prev[j] = i
        print(self.min_path_to_i[finish])
        #print(self.prev[finish])
        path = []
        j = finish
        while j is not None:
            path.append(j)
            j = self.prev[j]
        path = path[::-1]
        print(path)

G = WeightGraph([[0, 3, 5], [1, 2, 11], [2, 3, 56], [4, 3, 77], [4, 5, 89]])
G.min_path(0, 1)
