from helper import *

class PriorityQueue:
    def __init__(self):
        self.elements = []
    
    def empty(self):
        return len(self.elements) == 0
    
    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))
    
    def get(self):
        return heapq.heappop(self.elements)[1]

def get_heuristic(gate_start, gate_end): 
    x1, y1 = gate_start[0], gate_start[1]
    x2, y2 = gate_end[0], gate_end[1]
    return abs(x1 - x2) + abs(y1 - y2)

def search(graph, begin, end):
    border = PriorityQueue()
    border.put(begin, 0)
    cameFrom = {}
    costUpdate = {}
    cameFrom[begin] = None
    costUpdate[begin] = 0

    while not border.empty():
        current = border.get()

        if current == end:
            break

        for new in graph.edges(current):
            newCost = costUpdate[current] + graph.cost(current, new)
            if new not in costUpdate or newCost < costUpdate[new]:
                costUpdate[new] = newCost
                lead = newCost + get_heuristic(end, new)
                border.put(new, lead)
                cameFrom[new] = current
    return cameFrom, costUpdate



start, goal = (0, 4), (7, 8)
came_from, cost_so_far = search(diagram4, start, goal)
draw_grid(diagram4, width=3, point_to=came_from, start=start, goal=goal)
print()
draw_grid(diagram4, width=3, number=cost_so_far, start=start, goal=goal)
print()
