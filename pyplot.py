from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt


def z_function(x, y):
    print("joejoe")
    # print(np.sin(np.sqrt(x ** 2 + y ** 2)) * 0 )
    return np.sin(np.sqrt(x ** 2 + y ** 2)) * 0 

GridX = np.linspace(0, 25, 25)
GridY = np.linspace(0, 25, 25)
print(np.linspace(0,25,25))
X, Y = np.meshgrid(GridX, GridY)
Z = z_function(X, Y)

PlotLineX = np.linspace(0,5,2)
PlotLineY = np.linspace(0,1,1)
LineX, LineY = np.meshgrid(PlotLineX, PlotLineY)
LineZ = z_function(LineX, LineY)



fig = plt.figure()
ax = plt.axes(projection="3d")
ax.plot_wireframe(X, Y, Z, color='red')
ax.plot_wireframe(LineX, LineY, LineZ, color='green')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')

plt.show()