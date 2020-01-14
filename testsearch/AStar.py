from __future__ import print_function

class AStarGraph(object):
    # This defines a 3D grid

    def __init__(self):
        # These will be the gates and existing wires
        self.barriers = []
        
    def heuristic(self, start, end):
        # dx = absdiff(start[0], end[0])
        # dy = absdiff(start[1], end[1])
        # dz = absdiff(start[2], end[2])
        dx = abs(start[0] - end[0])
        dy = abs(start[1] - end[1])
        dz = abs(start[2] - end[2])
        dmin = min(dx, dy, dz)
        dmax = max(dx, dy, dz)
        dmid = dx + dy + dz - dmin - dmax
        D1 = 1
        D2 = 1
        D3 = 1
        
        return (D3 - D2) * dmin + (D2 - D1) * dmid + D1 * dmax
    
    def neighbours(self, cdn):
        n = []
        print("joejoe", cdn)

        # Allowed moves
        for dx, dy, dz in [(1,0,0), (-1,0,0), (0,1,0), (0,-1,0), (0,0,1), (0,0,-1)]:
            x2 = cdn[0] + dx
            y2 = cdn[1] + dy
            z2 = cdn[2] + dz
            if x2 < 0 or x2 > 4 or y2 < 0 or y2 > 4 or z2 < 0 or z2 > 7:
                continue
            n.append((x2, y2, z2))
        return n

    def move(self, a, b):
        # Make it really costly to move through barriers
        print("MOVE", a, b)
        for barrier in self.barriers:
            if b in barrier:
                return 99
        # Normal cost of movement
        return 1

def AStarSearch(start, end, graph):
     
    G = {}
    F = {}

    G[start] = 0
    F[start] = graph.heuristic(start, end)

    closedNodes = set()
    openNodes = set([start])

    original = {}

    while len(openNodes) > 0:
        current = None
        currentF = None
        
        for cdn in openNodes:
            print("cdn: ", cdn) 
            print("openNodes: ", len(openNodes))
            if current is None or F[cdn] < currentF:
                currentF = F[cdn]
                current = cdn
        
        if current == end:

            retrace = [current]
            while current in original:
                current = original[current]
                retrace.append(current)
            retrace.reverse()
            return path, F[end]
        openNodes.remove(current)
        try:
            closedNodes.remove(current)
        except:
            pass

        for neighbour in graph.neighbours(current):
            if neighbour in closedNodes:
                continue
            candidateG = G[current] + graph.move(current, neighbour)

            if neighbour not in openNodes:
                openNodes.add(neighbour)
            elif candidateG >= G[neighbour]:
                continue
            
            original[neighbour] = current
            G[neighbour] = candidateG
            H = graph.heuristic(neighbour, end)
            F[neighbour] = G[neighbour] + H
        
        # raise RuntimeError("No solution found")

if __name__ == "__main__":
    graph = AStarGraph()
    result, cost = AStarSearch((0,0,0), (2,3,0), graph)
    print("route: ", result)
    print("cost: ", cost)