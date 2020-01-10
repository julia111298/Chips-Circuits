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

class Graph():
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False
    
    def add_edge(self, u, v):
        if str(u) in self.vertices and str(v) in self.vertices:
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
        
        while len(queue) > 0:
            u = queue.pop(0)
            node_u = self.vertices[u]
            node_u.status = "visited"

            for v in node_u.neighbours:
                node_v = self.vertices[v]
                print("!", v, node_v.distance)
                if node_v.status == "unvisited":
                    queue.append(v)
                    print("V: ", v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


grid = []
# For 3D grid
# for x in range(4):
#     for y in range(4):
#         for z in range(4):
#             grid.append((x,y,z))
for x in range(2):
    for y in range(2):
        grid.append((x,y))

g = Graph()
a = Vertex("(0, 0)")
g.add_vertex(a)

# Or g.add_vertex(Vertex("B"))

# but for-loop is better:
# for i in range(ord("A"), ord("K")):
#     g.add_vertex(Vertex(chr(i)))

for i in grid:
    g.add_vertex(Vertex(str(i)))
    

edges = ["(0, 0)(1, 0)", "(0, 0)(0, 1)", "(1, 1)(0, 1)", "(1, 1)(1, 0)"]
for i in edges:
    g.add_edge(i[:6], i[6:])

# for i in range(len(grid)):
#     print(grid[i + 1])
#     break

# print(grid)
# edges = []
# for i in grid:
#     edges.append(i)

# new = []

# for i in edges:
#     for j in grid:
#         if j[0] - i[0] == 1 or j[0] - i[0] == -1 and j[1] - i[1] == 0:
#             if j[1] - i[1] == 1 or j[1] - i[1] == -1 and j[0] - i[0] == 0:
#                 new.append((i,j))

# print(new)

g.bfs(a)
g.print_graph()        

    
