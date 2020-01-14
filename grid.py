def grid():
    vertices = []
    for x in range(3):
        for y in range(3):
            for z in range(3):
                vertices.append((x, y, z))
    return vertices

print(grid())