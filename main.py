from code.visualisation import plot as plot


if __name__ == '__main__':
    plot.make_grid(5, 5)
    plot.draw_line([0,0,0], [1,1,1], "red")
    plot.plt.show()