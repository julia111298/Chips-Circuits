"""
Astar.py

Astar algorithm for getting the shortest route

Julia Linde, Tom Kamstra, Izhar Hamer
"""


def get_heuristic(gate_start, gate_end): 
    x1 = gate_start[0]
    y1 = gate_start[1]
    x2 = gate_end[0]
    y2 = gate_end[1]
    return abs(x1 - x2) + abs(y1 - y2)
