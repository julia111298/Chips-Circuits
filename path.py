"""
path.py

Tom Kamstra, Izhar Hamer, Julia Linde

Finds the optimal paths between the chips
"""

import csv

# Open file with netlist
data = open("netlist_1.csv")
reader = csv.reader(data)

# Create netlist
netlist = []

for net_1, net_2 in reader:
    net = (net_1, net_2)
    netlist.append(net)

# Open file with gates
gates = open("pritn_1.csv")
reader = csv.reader(gates)

# Create list for gate coordinates
gate_coordinates = []

for number, x, y in reader:
    try:
        x = int(x)
        y = int(y)
    except:
        x = x
        y = y
    coordinates = [x, y, 0]
    gate_coordinates.append(coordinates)

# Create dictionary of gate connections with corresponding shortest distance
distances = {}

for chip1, chip2 in netlist:
    if chip1 != "chip_a":
        gate_1 = int(chip1)
        gate_2 = int(chip2)
    
        connected_gate = (gate_1, gate_2)
    
        coordinate_start = gate_coordinates[gate_1]
        coordinate_end = gate_coordinates[gate_2]
    
        x_coordinate_1 = int(coordinate_start[0])
        y_coordinate_1 = int(coordinate_start[1])

        x_coordinate_2 = int(coordinate_end[0])
        y_coordinate_2 = int(coordinate_end[1])
    
        total_dist = abs(x_coordinate_1 - x_coordinate_2) + abs(y_coordinate_1 - y_coordinate_2)
    
        distances.update({connected_gate: total_dist})

# Sort connections from smallest to largest distance in dictionary
distances = list(distances.items())
for max_number in range(len(distances)-1, -1, -1):
    swapped = False
    for count in range(max_number):
        if distances[count][1] > distances[count + 1][1]:
            distances[count], distances[count + 1] = distances[count + 1], distances[count]
            swapped = True
    if not swapped:
        break

# Create dictionary of wires with connected gates
gate_connections = {}

# Connect gates with eachother, starting with smallest distance
for chips in distances:
    gate_1 = int(chips[0][0])
    gate_2 = int(chips[0][1])
    
    connected_gate = (gate_1, gate_2)

    coordinate = gate_coordinates[gate_1]
    coordinate_end = gate_coordinates[gate_2]

    x_coordinate_1 = int(coordinate[0])
    y_coordinate_1 = int(coordinate[1])
    z_coordinate_1 = int(coordinate[2])

    x_coordinate_2 = int(coordinate_end[0])
    y_coordinate_2 = int(coordinate_end[1])
    z_coordinate_2 = int(coordinate_end[2])

    wires = []

    while coordinate != coordinate_end:
        if x_coordinate_1 < x_coordinate_2:
            step_x = 1
        elif x_coordinate_1 > x_coordinate_2:
            step_x = -1
    
        if y_coordinate_1 < y_coordinate_2:
            step_y = 1
        elif y_coordinate_1 > y_coordinate_2:
            step_y = -1

        wires.append(coordinate)
    
        while x_coordinate_1 != x_coordinate_2:
            x_coordinate_1 = x_coordinate_1 + step_x
            coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
            # Check for other gates or other wires
            if gate_connections:
                for key in gate_connections:
                    selected_wires = gate_connections[key]
                    if coordinate in selected_wires or coordinate in gate_coordinates:
                        if coordinate != coordinate_end:
                            x_coordinate_1 = x_coordinate_1 - step_x
                            # z kan nu niet meerdere stappen omhoog/omlaag
                            z_coordinate_1 = z_coordinate_1 + 1
                            #checken of na deze stap geen gate zit
                            break
            elif coordinate in gate_coordinates and coordinate != coordinate_end:
                x_coordinate_1 = x_coordinate_1 - step_x
                # z kan nu niet meerdere stappen omhoog/omlaag
                z_coordinate_1 = z_coordinate_1 + 1
                #checken of na deze stap geen gate zit
    
            coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
            wires.append(coordinate)

            if x_coordinate_1 == x_coordinate_2 and y_coordinate_1 == y_coordinate_2:
                while z_coordinate_1 != z_coordinate_2:
                    z_coordinate_1 = z_coordinate_1 - 1
                    coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                    wires.append(coordinate)

        while y_coordinate_1 != y_coordinate_2:
            y_coordinate_1 = y_coordinate_1 + step_y
            coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
            # Check for other gates or other wires
            if gate_connections:
                for key in gate_connections:
                    selected_wires = gate_connections[key]
                    if coordinate in selected_wires or coordinate in gate_coordinates:
                        if coordinate != coordinate_end:
                            y_coordinate_1 = y_coordinate_1 - step_y
                            # z kan nu niet meerdere stappen omhoog/omlaag
                            z_coordinate_1 = z_coordinate_1 + 1
                            #checken of na deze stap geen gate zit
                            break
            elif coordinate in gate_coordinates and coordinate != coordinate_end:
                y_coordinate_1 = y_coordinate_1 - step_y
                # z kan nu niet meerdere stappen omhoog/omlaag
                z_coordinate_1 = z_coordinate_1 + 1
                #checken of na deze stap geen gate zit

            coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
            wires.append(coordinate)
    
            if x_coordinate_1 == x_coordinate_2 and y_coordinate_1 == y_coordinate_2:
                while z_coordinate_1 != z_coordinate_2:
                    z_coordinate_1 = z_coordinate_1 - 1
                    coordinate = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                    wires.append(coordinate)
                    
    gate_connections.update({connected_gate: wires})
print(gate_connections)
print("JOEJOE")
print(gate_connections[(16,6)])