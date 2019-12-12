from collections import defaultdict


class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def printGraph(self):
        for i in self.graph:
            print(i, self.graph[i])

    def TraverseGraphBreathWay(self, s):
        vertices = [False] * (len(self.graph))
        vertices[s] = True

        queue = []
        queue.append(s)

        while queue:
            s = queue.pop(0)
            print(s, end=" ")

            for i in self.graph[s]:
                # print(vertices, i)
                if vertices[i] == False:
                    vertices[i] = True
                    queue.append(i)

    def TraverseGraphDeepWay(self, s):
        vertices = [False] * (len(self.graph))

        self.TraverseGraphDeep(s, vertices)

    def TraverseGraphDeep(self, s, vertices):
        vertices[s] = True
        print(s, end=" ")

        for v in self.graph[s]:
            if vertices[v] == False:
                self.TraverseGraphDeep(v, vertices)


g = Graph()

# g.addEdge(0, 1)
# g.addEdge(0, 2)
# g.addEdge(1, 2)
# g.addEdge(2, 0)
# g.addEdge(2, 3)
# g.addEdge(3, 3)
# g.addEdge(3, 4)
# g.addEdge(4, 0)

g.addEdge(0, 1)
g.addEdge(0, 2)
g.addEdge(1, 2)
g.addEdge(2, 0)
g.addEdge(2, 3)
g.addEdge(3, 3)

g.printGraph()

g.TraverseGraphBreathWay(2)
print("\n")
g.TraverseGraphDeepWay(2)

# This is Python 2
import sys
