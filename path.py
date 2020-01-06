"""
path.py

Tom Kamstra, Izhar Hamer, Julia Linde

Finds the optimal paths between the chips
"""

import csv

data = open("netlist_1.csv")
reader = csv.reader(data)

netlist = []

for net_1, net_2 in reader:
    listje = (net_1, net_2)
    netlist.append(listje)
    
print(netlist)

gates = open("pritn_1.csv")
reader = csv.reader(gates)

gate_coordinates = []

for number, x, y in reader:
    listje = [x, y, 0]
    gate_coordinates.append(listje)

print("GATE COORDINATES")
print(gate_coordinates)
