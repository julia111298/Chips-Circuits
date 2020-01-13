class Vertex():
    def __init__(self, name):
        self.name = name
        self.neighbours = []
        self.distance = 9999
        self.status = "unvisited"
    
    def add_neighbour(self, v):
        if v not in self.neighbours:
            self.neighbours.append(v)
            self.neighbours.sort()
            print("neighbours:", self.neighbours)

class Graph():
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbour(v)
                if key == v:
                    value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + " " + str(self.vertices[key].distance))
    
    def bfs(self, vert):
        queue = list()
        vert.distance = 0
        vert.status = "visited"
        for v in vert.neighbours:
            self.vertices[v].distance = vert.distance + 1
            queue.append(v)
        print("Q: ", queue)
        
        while len(queue) > 0:
            print("Q1: ", queue)
            u = queue.pop(0)
            print("Q2: ", queue)
            node_u = self.vertices[u]
            node_u.status = "visited"

            for v in node_u.neighbours:
                node_v = self.vertices[v]

                if node_v.status == "unvisited":
                    queue.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1

g = Graph()
a = Vertex("A")
g.add_vertex(a)

# Or g.add_vertex(Vertex("B"))

# but for loop is better:
for i in range(ord("A"), ord("K")):
    g.add_vertex(Vertex(chr(i)))

edges = ["AB", "AE", "BF", "CG", "DE", "DH", "EH", "FG", "FI", "FJ", "GJ", "HI"]
for i in edges:
    g.add_edge(i[:1], i[1:])


g.bfs(a)
g.print_graph()        

    
