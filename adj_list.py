class Graph:
    def __init__(self,v):
        self.v=v
        self.adj_list={i: [] for i in range(v)}

    def add_edge(self, u, v,w):
        self.adj_list[u].append((v,w))
        self.adj_list[v].append((u,w))
    def print_graph(self):
        for i in self.adj_list:
            print(i, "->", " -> ".join(map(str, self.adj_list[i])))

# Example usage:
v=5
g = Graph(v)
g.add_edge(0, 1,3)
g.add_edge(0, 2,5)
g.add_edge(3,4,6)
g.add_edge(0,4,7)
g.add_edge(4,1,11)
g.add_edge(1,3,2)
g.add_edge(2,3,10)

g.print_graph()
