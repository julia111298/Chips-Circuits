from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    print("joejoe")

    # return np.sin(np.pi/2) * np.sqrt(x ** 2 + y ** 2)
    return (np.sin(np.sqrt(x ** 2 + y ** 2)) * 0) + 1

# GridX = np.linspace(0, 25, 25)
# GridY = np.linspace(0, 25, 25)

# print(np.linspace(0,25,25))
# X, Y = np.meshgrid(GridX, GridY)
# Z = z_function(X, Y)
# print(Z)


def make_grid(layers, size):
    for i in range(layers): 
        GridX = np.linspace(0, size, (size + 1))
        GridY = np.linspace(0, size, (size + 1))
        X, Y = np.meshgrid(GridX, GridY)
        Z = (np.sin(np.sqrt(X ** 2 + Y ** 2)) * 0) + i
        # Plot grid
        ax.plot_wireframe(X, Y, Z, lw=0.5,  color='grey')

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

PointX = [2, 1, 3, 5, 4]
PointY = [0, 1, 2, 5, 4]
PointZ = [0, 0, 0, 0, 0]

# Xline = [2, 2, 1]
# Yline = [0, 1, 1]
# Zline = [0, 0, 0]

fig = plt.figure()
ax = plt.axes(projection="3d")

set_gate([2, 0, 0])
set_gate([1, 1, 0])

make_grid(5, 5)

draw_line([1,1,0], [1,0,0])
draw_line([1,0,0], [2,0,0])



# Draw line
# ax.plot(Xline, Yline, Zline,lw=3,  color='blue', ms=12)


# a = np.ndarray(shape=(2,2), dtype=float, order='F')
# print(a)
# ax.plot_wireframe(a, LineY, LineZ, color='green')
# ax.plot_wireframe([[0. 0.]], [[0. 5.]], [[0. -0.]], color='blue')


ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

#configure axes
ax.set_zlim3d(0, 5)
ax.set_xlim3d(0, 5)
ax.set_ylim3d(0, 5)

plt.show()