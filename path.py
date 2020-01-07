"""
path.py

Tom Kamstra, Izhar Hamer, Julia Linde

Finds the optimal paths between the chips
"""

import csv

data = open("netlist_1.csv")
reader = csv.reader(data)

# Create netlist
netlist = []

for net_1, net_2 in reader:
    listje = (net_1, net_2)
    netlist.append(listje)

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
    listje = [x, y, 0]
    gate_coordinates.append(listje)

print("gateeee coordinates")
print(gate_coordinates)
# Create wires with connections
gate_connections = {}

# Create gate connections with corresponding shortest distance
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

print("JOEJOE")
print(distances)


# for key, value in distances.items():
#     if distances[key] > distances[key + 1]:
#         temporary = distances[key]
#         distances[key] = distances[key + 1]
#         distances[key + 1] = temporary

distances = list(distances.items())
for mx in range(len(distances)-1, -1, -1):
    swapped = False
    for i in range(mx):
        if distances[i][1] > distances[i+1][1]:
            distances[i], distances[i+1] = distances[i+1], distances[i]
            swapped = True
    if not swapped:
        break

print("JOEJOEEEE")
print(distances)

for chip1, chip2 in netlist:
    print("CHIP 1!!!!\n")
    print(chip1)
    if chip1 != "chip_a":
        gate_1 = int(chip1)
        gate_2 = int(chip2)
        
        connected_gate = (gate_1, gate_2)

        coordinate_start = gate_coordinates[gate_1]
        coordinate_end = gate_coordinates[gate_2]
        print("BEGIN COORDINATE")
        print(coordinate_start)
        print("END COORDINATE")
        print(coordinate_end)

        x_coordinate_1 = int(coordinate_start[0])
        y_coordinate_1 = int(coordinate_start[1])
        z_coordinate_1 = int(coordinate_start[2])

        x_coordinate_2 = int(coordinate_end[0])
        y_coordinate_2 = int(coordinate_end[1])
        z_coordinate_2 = int(coordinate_end[2])

        wires = []

        while coordinate_start != coordinate_end:
            if x_coordinate_1 < x_coordinate_2:
                step_x = 1
            elif x_coordinate_1 > x_coordinate_2:
                step_x = -1
        
            if y_coordinate_1 < y_coordinate_2:
                step_y = 1
            elif y_coordinate_1 > y_coordinate_2:
                step_y = -1

            wires.append(coordinate_start)
        
            while x_coordinate_1 != x_coordinate_2:
                x_coordinate_1 = x_coordinate_1 + step_x
                coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                # Check for other gates or other wires
                if gate_connections:
                    for key in gate_connections:
                        selected_wires = gate_connections[key]
                        if coordinate_start in selected_wires or coordinate_start in gate_coordinates:
                            if coordinate_start != coordinate_end:
                                x_coordinate_1 = x_coordinate_1 - step_x
                                # z kan nu niet meerdere stappen omhoog/omlaag
                                z_coordinate_1 = z_coordinate_1 + 1
                                #checken of na deze stap geen gate zit
                                break
                elif coordinate_start in gate_coordinates and coordinate_start != coordinate_end:
                    x_coordinate_1 = x_coordinate_1 - step_x
                    # z kan nu niet meerdere stappen omhoog/omlaag
                    z_coordinate_1 = z_coordinate_1 + 1
                    #checken of na deze stap geen gate zit
        
                
                coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                # if coordinate gelijk aan andere: doe - step_x en y_coordinate + step_y
                wires.append(coordinate_start)
    
                if x_coordinate_1 == x_coordinate_2 and y_coordinate_1 == y_coordinate_2:
                    while z_coordinate_1 != z_coordinate_2:
                        z_coordinate_1 = z_coordinate_1 - 1
                        coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                        wires.append(coordinate_start)
    

            while y_coordinate_1 != y_coordinate_2:
                y_coordinate_1 = y_coordinate_1 + step_y
                coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                # Check for other gates or other wires
                if gate_connections:
                    for key in gate_connections:
                        selected_wires = gate_connections[key]
                        if coordinate_start in selected_wires or coordinate_start in gate_coordinates:
                            if coordinate_start != coordinate_end:
                                y_coordinate_1 = y_coordinate_1 - step_y
                                # z kan nu niet meerdere stappen omhoog/omlaag
                                z_coordinate_1 = z_coordinate_1 + 1
                                #checken of na deze stap geen gate zit
                                break
                elif coordinate_start in gate_coordinates and coordinate_start != coordinate_end:
                    y_coordinate_1 = y_coordinate_1 - step_y
                    # z kan nu niet meerdere stappen omhoog/omlaag
                    z_coordinate_1 = z_coordinate_1 + 1
                    #checken of na deze stap geen gate zit
    
                coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                # if coordinate gelijk aan andere: doe - step_y en x_coordinate + step_x
                wires.append(coordinate_start)
        
                if x_coordinate_1 == x_coordinate_2 and y_coordinate_1 == y_coordinate_2:
                    while z_coordinate_1 != z_coordinate_2:
                        z_coordinate_1 = z_coordinate_1 - 1
                        coordinate_start = [x_coordinate_1, y_coordinate_1, z_coordinate_1]
                        wires.append(coordinate_start)

    
        print("NEW WIRES")
        print(wires)
        gate_connections.update({connected_gate: wires})
print(gate_connections)
# print("JOEJOE")
# print(gate_connections[(16,6)])