class Graph:
    def __init__(self):
        self.adj_list = {}

    def addVertex(self,vertex):
        if vertex not in self.adj_list:
            self.adj_list[vertex] = []

    def addEdge(self,v1,v2):
        if v1 in self.adj_list and v2 in self.adj_list:
                self.adj_list[v1].append(v2)
                self.adj_list[v2].append(v1) # Only for Undirected Graph
                
    def displayGraph(self):
        if not self.adj_list :
             print("The Graph is empty")
             return
        for vertex in self.adj_list:
            print(f"vertex: {self.adj_list[vertex]}")
        return

    def depthFirstSearch(self,start_node,visited=None):
        if visited is None:
              visited = set()
        print(start_node, '->',end=' ')
        visited.add(start_node)
        for neighbor in self.adj_list[start_node]:
             if neighbor not in visited:
                  self.depthFirstSearch(neighbor,visited)
    