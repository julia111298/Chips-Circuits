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

path = []

node_previous = []
temp = 0

while open_list:
    
    
    # q = min(open_list, key=)

    # Alle opties met de minimum f waarde pakken?hi
    f_list = []
    for i in open_list:
        f_list.append(i.f_score())
    minimum = min(f_list)
    for i in range(len(f_list)):
        if f_list[i] == minimum:
            q = open_list[i]
    # print("QQQ", q)
    temp += 1
    if temp == 3:
        break
    
    if str(q) == str(goal):
        print(path)
        print("finished")
        break

    # open_list.remove(q)
    # closed_list.append(q)
    
    # blocked.append(q)
    # print("closed: : :", closed_list)
    successors = q.successors(grid, q, closed_list)
    
    # blocked.append(q)
    # print("blcoked,: ", blocked)
    # print("prev", node_previous)

    if node_previous:
        successors.pop(0)
    
    print(q, " successors: ", successors)
    node_previous.clear()
    node_previous.append(q)
        


    # print("open!", open_list)

    for i in successors:
        # g_counter += 1

        # i.g_score(1)
        # i.h_score(i, q)
        # f = i.f_score()

        successor_current_cost = q.get_g()
        print("i: ", i)
        print("open lisT", open_list, "closed:", closed_list)
        if i in open_list:
            print("getggg: ", i.get_g())
            print("current cost succ: ", successor_current_cost)
            if i.get_g() <= successor_current_cost:
                # path.append(i)
                # print("true")
                # open_list.remove(i)
                break

        elif i in closed_list:
            print("in closed")
            if i.get_g() <= successor_current_cost:
                break
            closed_list.remove(i)
            open_list.append(i)
        
        else:
            open_list.append(i)
            # i.g_score(1)
            # i.h_score(i, goal)
            # i.f_score()
            i.h_score(i, goal)
        
        i.set_g(successor_current_cost)
        q = i
    open_list.remove(q)
    closed_list.append(q)


print("not finished")