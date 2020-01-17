"""
functions.py

Tom Kamstra, Izhar Hamer, Julia Linde

Defines functions needed for the script.
"""

def create_steps(x_start, x_end, y_start, y_end):
    step_x = 1
    step_y = 1
    
    if x_start > x_end:
        step_x = -1

    if y_start > y_end:
        step_y = -1

    return [step_x, step_y]
    
def change_coor(gate_conn, coor, gate_coor, wires, coor_end, coor_start1, step1, coor_start2, step2):
    for key in gate_conn:
        selected_wires = gate_conn[key]
        if coor in selected_wires or coor in gate_coor or coor in wires:
            if coor != coor_end:
                coor_start1 = coor_start1 - step1
                coor_start2 = coor_start2 + step2
                break
                
    return [coor_start1, coor_start2]