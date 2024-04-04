class Graph:
    def __init__(self,v):
        self.v=v
        self.graph=[]
        self.graph=[[[0]*v] for i in range(v)]
    def add_edge(self,u,v,w):
        self.graph[u][v]=w
        self.graph[v][u]=w
    def print(self):
        for i in self graph:
            print(" ".join(map(str,i)))
g=Graph()
v=5
g.add_edge(0,1,3)
g.add_edge(1,2,5)
g.add_edge(3,4,6)
g.add_edge(0,4,7)
g.add_edge(4,1,11)
g.add_edge(1,3,7)
g.add_edge(2,3,10)
g.print()