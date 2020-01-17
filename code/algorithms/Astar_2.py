##################################################
# Astar_2.py
# 
# By team De Madarijntjes
# 
# Pseudocode source: https://www.geeksforgeeks.org/a-search-algorithm/
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

    def f_score(self):
        return self.g + self.h
    
    def g_score(self, value):
        self.g = value
        return self.g
    
    def h_score(self, current, goal):
        self.h = abs(current.x - goal.x) + abs(current.y - goal.y)
        
        return self.h
    

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
start.g_score(0)
start.h_score(start, Node(1, 1))

open_list = [start]
closed_list = []

# Make sure successors aren't f'ed up
blocked = []
g_counter = 0

path = []

while open_list:
    

    # q = min(open_list, key=)
    f_list = []
    for i in open_list:
        f_list.append(i.f_score())
    minimum = min(f_list)
    for i in range(len(f_list)):
        if f_list[i] == minimum:
            q = open_list[i]

    
    if str(q) == str(goal):
        print(path)
        print("finished")

    open_list.remove(q)
    closed_list.append(q)
    
    
    blocked.append(q)
    successors = q.successors(grid, q, blocked)

    for i in successors:
        g_counter += 1
        if i in closed_list:
            continue
        i.g_score(g_counter)
        i.h_score(i, q)
        f = i.f_score()
        if i in open_list and f < i.g_score(i.g_score(g_counter) + 1):
            # path.append(q)
            print("true")
            open_list.remove(i)

        elif i in closed_list and f < i.g_score(i.g_score(g_counter) + 1):
            print("JOEJOE")
            closed_list.remove(i)
        
        elif i not in open_list and i not in closed_list:
            open_list.append(i)
            i.g_score(f)
            i.h_score(i, goal)
            i.f_score()
            


