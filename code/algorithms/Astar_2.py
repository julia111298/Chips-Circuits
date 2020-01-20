##################################################
# Astar_2.py
# 
# By team De Madarijntjes
# 
# Pseudocode source: https://www.geeksforgeeks.org/a-search-algorithm/
# and http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
##################################################
class Grid():
    def __init__(self, grid_size):
        self.grid_size = grid_size
        self.grid = []
        self.g = 0

    def make_grid(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                self.grid.append(Node(i, j))
    
    def get_grid(self):
        return self.grid
        

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.g = 0
        self.parent = None

    def f_score(self):
        return self.g + self.h
    
    def get_g(self):
        return self.g
    
    def set_g(self, value):
        self.g = value
    
    def g_score(self, value):
        self.g += value
    
    def h_score(self, current, goal):
        self.h = abs(current.x - goal.x) + abs(current.y - goal.y)
        
        return self.h
    
    def set_parent(self, node):
        self.parent = node
    
    def get_parent(self):
        return self.parent

    def successors(self, grid, node_current, blocked):
        self.node_successors = []
        for i in grid:
            for j in grid:
                if i.x == node_current.x and i.y == node_current.y:
                    if abs(j.x - i.x) == 1 and j.y - i.y == 0:   
                        if j not in blocked: 
                            self.node_successors.append(j)
                    elif abs(j.y - i.y) == 1 and j.x - i.x == 0:
                        if j not in blocked:
                            self.node_successors.append(j)
        return self.node_successors

    def __repr__(self):
        return str([self.x, self.y])


grid = Grid(3)
grid.make_grid()
grid = grid.get_grid()

start = Node(0, 0)
goal = Node(2, 2)
start.h_score(start, goal)

open_list = [start]
closed_list = []

# Make sure successors aren't f'ed up
blocked = []
g_counter = 1



node_previous = []

while open_list:
    # Alle opties met de minimum f waarde pakken?
    f_list = []
    for i in open_list:
        f_list.append(i.f_score())
    minimum = min(f_list)
    for i in range(len(f_list)):
        if f_list[i] == minimum:
            q = open_list[i]
    
    print("QQQ", q, "open list: ", open_list, "closed list: ", closed_list)
    if str(q) == str(goal):
        print("finished")
        break

    successors = q.successors(grid, q, closed_list)

    
    if node_previous and successors:
        successors.pop(0)
    
    # print(q, " successors: ", successors)
    node_previous.clear()
    node_previous.append(q)
        

    for i in successors:

        # Set successor_current_cost = g(node_current) + w(node_current, node_successor)
        successor_current_cost = q.get_g() + 1
        # print("i: ", i)
        # print("open lisT", open_list, "closed:", closed_list)
        if i in open_list:
            # print("getggg: ", i.get_g())
            # print("current cost succ: ", successor_current_cost)
            if i.get_g() <= successor_current_cost:
                # print("true")
                # open_list.remove(i)
                break

        elif i in closed_list:
            if i.get_g() <= successor_current_cost:
                break
            closed_list.remove(i)
            open_list.append(i)
        
        else:
            open_list.append(i)
            i.h_score(i, goal)
        
        i.set_g(successor_current_cost)
        i.set_parent(q)
    
    open_list.remove(q)
    closed_list.append(q)

end = q
path = []

while end.get_parent() != None:
    end = end.get_parent()
    path.append(end)

# for q.get_parent()
# print(q.get_parent().get_parent())

print(path)