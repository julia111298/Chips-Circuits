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
    try:
        x = int(x)
        y = int(y)
    except:
        x = x
        y = y
    listje = [x, y, 0]
    gate_coordinates.append(listje)

for chip1, chip2 in netlist:
    try:
        gate_1 = int(chip1)
        gate_2 = int(chip2)

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
                if coordinate_start in gate_coordinates and coordinate_start != coordinate_end:
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
                if coordinate_start in gate_coordinates and coordinate_start != coordinate_end:
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
    except:
        print("HELLO")