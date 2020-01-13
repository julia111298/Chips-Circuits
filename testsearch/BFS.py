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
                print("@@: ", u, v) 
                print(key)
                if key == u:
                    print("true1")
                    value.add_neighbour(v)
                if key == v:
                    print("true2")
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
                # print("!", v, node_v.distance)
                if node_v.status == "unvisited":
                    queue.append(v)
                    # print("V: ", v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


grid = []
for x in range(2):
    for y in range(2):
        grid.append((x,y))

g = Graph()
a = Vertex("(0, 0)")
g.add_vertex(a)


for i in grid:
    g.add_vertex(Vertex(str(i)))
    

edges = []
for i in grid:
    edges.append(i)

new = []

for i in edges:
    for j in grid:
        if abs(j[0] - i[0]) == 1 and j[1] - i[1] == 0:
            if (j,i) not in new:
                new.append((i,j))
        elif abs(j[1] - i[1]) == 1 and j[0] - i[0] == 0:
            if (j,i) not in new:
                new.append((i,j))

for i in new:
    g.add_edge(str(i[0]), str(i[1]))

print()





print(g.vertices)


g.bfs(a)
g.print_graph()        

    
