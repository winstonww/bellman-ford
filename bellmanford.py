import sys
from collections import defaultdict


class Node:
    def __init__(self, key):
        self.key = key

    def __repr__(self):
        return self.key
    
    def __hash__(self):
        return hash(self.key)
    
    def __eq__(self, other):
        return other.key == self.key

    def __lt__(self, other):
        return self.key > other.key 


# graph is an adjacency matrix
class Graph:
    def __init__(self, graph):
        self.graph = graph

    def __iter__(self):
        for v in self.graph:
            yield v

    def __getitem__(self, key):
        return self.graph[key]

    def __len__(self):
        return len(self.graph)

        
class BellmanFord(object):
    def __init__(self, graph):
        self.graph = graph
        self.distMatrix = None

    def _init_dist(self, start):
        self.distMatrix = defaultdict(lambda: sys.maxsize)
        for dst, w in self.graph[start].items():
            self.distMatrix[dst] = w
        
    def run(self, start, end):
        self._init_dist(start)
        for i in range(len(self.graph)):
            for src in self.graph:
                for dst, weight in self.graph[src].items():
                    if self.distMatrix[src] + weight < self.distMatrix[dst]:
                        self.distMatrix[dst] = self.distMatrix[src] + weight
        return self.distMatrix[end]

g = Graph({
    Node('A'): dict([(Node('B'), 3), (Node('C'), 6)]),
    Node('B'): dict([(Node('D'), 4), (Node('E'), 10)]),
    Node('C'): dict([(Node('D'), 2)]),
    Node('D'): {Node('E'): 5},
    Node('E'): {}
})

d = BellmanFord(g)
res = d.run(Node('A'), Node('E'))
print(res)

