###########################################################################
# A* search algorithm
# 
# By team De Mandarijntjes
# 
# Pseudocode from http://mat.uab.cat/~alseda/MasterOpt/AStar-Algorithm.pdf
#             and https://en.wikipedia.org/wiki/A*_search_algorithm
###########################################################################

# function reconstruct_path(cameFrom, current)
#     total_path := {current}
#     while current in cameFrom.Keys:
#         total_path.prepend(current)
#         current := cameFrom[current]
#     return total_path


def heuristic(currentCell, goal):
    return abs(currentCell.x - goal.x) + abs(currentCell.y - goal.y)

class Node():
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def f_score(self):
        h = self.h_score()
        return self.g + h
    
    def g_score(self, value):
        self.g = value
        return self.g
    
    def h_score(self):
        self.h = heuristic(Node(self.x, self.y), Goal(1, 1))
        
        return self.h
    
    def successors(self, grid, node_current, successor_list):
        node_successors = []
        # print("!!!!! successor_list", successor_list)
        for i in successor_list:
            print("plop", i)
            for j in i:
                print("***", j.x, j.y)
            print()
        for i in grid:
            for j in grid:
                # Kan mooier?
                if i.x == node_current.x and i.y == node_current.y:
                    if abs(j.x - i.x) == 1 and j.y - i.y == 0:    
                        if [j,i] not in successor_list:
                            print("-_-", [j.x, j.y, i.x, i.y])
                            node_successors.append((j))
                    elif abs(j.y - i.y) == 1 and j.x - i.x == 0:
                        if [j,i] not in successor_list:
                            print("---", [j.x, j.y, i.x, i.y])
                            node_successors.append((j))
        return node_successors
    

class Goal():
    def __init__(self, x, y):
        self.x = x
        self.y = y

# class Gscore():
#     def __init__(self, node):
        



grid = []

grid_size = 2
for x in range(grid_size):
    for y in range(grid_size):
        grid.append(Node(x, y))


open_list = []
closed_list = []

node_start = Node(0, 0)
node_goal = Node(1, 1)

open_list.append(node_start)

node_start.g_score(0)

# weight of move, could be used to indicated another wire or gate with extremely high value
w = 1

# temp counter to stop list
temp_count = 0

successor_list = []

while open_list:
    # print()
    for i in open_list:
        print("open list", i.x, i.y)
    print()

    # Take the node with the lowest f TODO
    # Get node with minimum f score, could be done better with min()
    f_list = []
    for i in open_list:
        f_list.append(i.f_score())
    minimum = min(f_list)
    for i in range(len(f_list)):
        if f_list[i] == minimum:
            node_current = open_list[i]
    print("  node current:     ", node_current.x, node_current.y)

    if node_current == node_goal:
        print("Found solution")
        break
    # print("node_current successors", node_current.successors(grid, node_current))
    # for i in node_current.successors(grid, node_current):
    #     print("!!!!", i.x, i.y)
    for i in node_current.successors(grid, node_current, successor_list):
        print("iiii", i.x, i.y)
        successor_list.append([node_current, i])
        successor_current_cost = node_current.g + w
        
        if i in open_list:
            print(":::1:::")
            if i.g <= successor_current_cost:
                print(":::2:::")
                break
        elif i in closed_list:
            print(":::3:::")
            if i.g <= successor_current_cost:
                print(":::4:::")
                break
            # in the above if statement?
            closed_list.remove(i)
            open_list.append(i)
        else:
            print(":::5:::")
            open_list.append(i)
            i.h_score()
            print("len openlist", len(open_list))
        i.g_score(successor_current_cost)
        node_current = i
    # ???
    print(node_current.x, node_current.y, "current")
    # open_list.remove(node_current)
    closed_list.append(node_current)

    temp_count += 1
    if temp_count == 4:
        break

if node_current != node_goal:
    print("error, open_list is empty!")
else:
    print("success?")
    

    




