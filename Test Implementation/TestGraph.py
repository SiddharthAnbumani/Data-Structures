"""
Implementation of Graph
"""

class Graph:
    def __init__(self):
        self.adj_list = {}
    def addVertex(self,vertex):
        self.adj_list[vertex] = []
    def addEdges(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1) # If cyclic
    def DepthFirstSearch(self,start_node,visited = None):
        if visited is None:
            visited = set()
        print(start_node, end="")
        visited.add(start_node)
        for neighbor in self.adj_list[start_node]:
            if neighbor  not in visited:
                self.DepthFirstSearch(neighbor,visited)
    def BreadthFirstSearch(self,start_node):
        visited = set()
        queue = []
        visited.add(start_node)
        queue.append(start_node)
        while queue:
            current = queue.pop(0)
            print(current,'->',end='')
            for neighbor in self.adj_list[current]:
                 if neighbor not in visited:
                      visited.add(neighbor)
                      queue.append(neighbor)

