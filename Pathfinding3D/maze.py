import random
import mcpi.block as block


def setMaze(maze, n, mc):
    wall = (95, 8)
    possible_move = block.AIR
    end = 133
    start = block.DIAMOND_BLOCK

    for i in range(n):
        for j in range(n):
            for z in range(n):
                if maze[i][j][z] == "#":
                    mc.setBlock(j, z, i,wall[0], wall[1] )
                elif maze[i][j][z] == "X":
                    mc.setBlock(j, z, i, end)
                elif maze[i][j][z] == "0":
                    mc.setBlock(j, z, i, start)
                else:
                    mc.setBlock(j, z, i, possible_move)


def createMaze3d(n, r):
    maze = []

    for i in range(n):
        maze.append([])
        for j in range(n):
            maze[i].append([])
            for k in range(n):
                temp = random.randint(0, 100)
                if temp < r * 100:
                    maze[i][j].append("#")
                else:
                    maze[i][j].append(" ")

    x_start, y_start, z_start = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1)
    maze[x_start][y_start][z_start] = "0"

    x_stop, y_stop, z_stop = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1)
    while x_stop == x_start and y_stop == y_start and z_stop == z_start:
        x_stop, y_stop, z_stop = random.randint(0, n-1), random.randint(0, n-1), random.randint(0, n-1)
    maze[x_stop][y_stop][z_stop] = "X"

    return maze


def exampleMaze3dRods(n, d):
    d = d * n * n
    l = int(d)
    maze = []
    for i in range(n):
        maze.append([])
        for j in range(n):
            maze[i].append([])
            for k in range(n):
                maze[i][j].append(" ")
    used = []
    while l > 0:
        x = random.randint(1, n-1)
        y = random.randint(1, n-1)
        if [x,y] not in used:
            used.append([x,y])
            l-=1

    for coord in used:
        for j in range(n):
            hole_chance = random.randint(1, 20)
            if hole_chance != 1:
                maze[coord[0]][j][coord[1]] = "#"
    maze[5][5][5] = "0"
    maze[n - 5][n - 5][n - 5] = "X"

    return maze
