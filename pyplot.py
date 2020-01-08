from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


def make_grid(layers, size):
    for i in range(layers): 
        GridX = np.linspace(0, size, (size + 1))
        GridY = np.linspace(0, size, (size + 1))
        X, Y = np.meshgrid(GridX, GridY)
        Z = (np.sin(np.sqrt(X ** 2 + Y ** 2)) * 0) + i
        # Plot grid
        ax.plot_wireframe(X, Y, Z, lw=0.5,  color='grey')
    #configure axes
    ax.set_zlim3d(0, layers)
    ax.set_xlim3d(0, size)
    ax.set_ylim3d(0, size)

# Enter coordinates as list with: [X, Y, Z]
def draw_line(crdFrom, crdTo):
    Xline = [crdFrom[0], crdTo[0]]
    Yline = [crdFrom[1], crdTo[1]]
    Zline = [crdFrom[2], crdTo[2]]
    # Draw line
    ax.plot(Xline, Yline, Zline,lw=3,  color='blue', ms=12)

def set_gate(crd):
    PointX = [crd[0]]
    PointY = [crd[1]]
    PointZ = [crd[2]]
    # Plot points
    ax.plot(PointX, PointY, PointZ, ls="None", marker="o", color='red')

fig = plt.figure()
ax = plt.axes(projection="3d")

make_grid(5, 5)

set_gate([2, 0, 0])
set_gate([1, 1, 0])
set_gate([3, 3, 0])

draw_line([1,1,0], [1,0,0])
draw_line([1,0,0], [2,0,0])

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()