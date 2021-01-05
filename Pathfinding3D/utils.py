import time
import mcpi.block as block


def plac(x, y, z, roz, mc):
    mc.setBlocks(x, y, z, x + roz, y + 10, z + roz, block.AIR)
    mc.setBlocks(x, y, z, x + roz, y - 1, z + roz, block.STONE)


def setMove(v, n, mc):
    x, y, z = v_to_xyz(v, n)
    mc.setBlock(y, z, x, 95, 4)
    time.sleep(0.005)


def v_in_Q(ngb):
    Q = []
    for i in range(len(ngb)):
        if ngb[i] != []:
            Q.append(i)
    return Q


def min_in_Q(Q, d):
    m = d[Q[0]]
    v = Q[0]
    for i in Q:
        if d[i] < m:
            m = d[i]
            v = i
    if m == 1000:
        return -1
    return v


def ngb_from_maze(maze, n):
    ngb = [[] for _ in range(n * n * n)]

    for i in range(n * n * n):
        x, y, z = v_to_xyz(i, n)
        if maze[x][y][z] == "#":
            continue
        else:
            temp = i % (n * n)
            if temp % n == n - 1:
                continue
            else:
                x, y, z = v_to_xyz(i + 1, n)
                if maze[x][y][z] == "#":
                    continue
                else:
                    ngb[i].append(i + 1)
                    ngb[i + 1].append(i)

    for i in range(n * n * n):
        x, y, z = v_to_xyz(i, n)
        if maze[x][y][z] == "#":
            continue
        else:
            temp = i % (n * n)
            temp = temp // n
            if temp % n == n - 1:
                continue
            else:
                x, y, z = v_to_xyz(i + n, n)
                if maze[x][y][z] == "#":
                    continue
                else:
                    ngb[i].append(i + n)
                    ngb[i + n].append(i)

    for i in range(n * n * n - n * n):
        x, y, z = v_to_xyz(i, n)
        if maze[x][y][z] == "#":
            continue
        else:
            x, y, z = v_to_xyz(i + n * n, n)
            if maze[x][y][z] == "#":
                continue
            else:
                ngb[i].append(i + n * n)
                ngb[i + n * n].append(i)

    return ngb


def xyz_to_v(x, y, z, n):
    return z * n * n + y * n + x


def v_to_xyz(v, n):
    z = v // (n * n)
    temp = v % (n * n)
    y = temp // n
    x = temp % n
    return x, y, z


def find_start_stop(maze, n):
    start, stop = 0, 0
    for i in range(n):
        for j in range(n):
            for z in range(n):
                if maze[i][j][z] == "0":
                    start = [i, j, z]
                elif maze[i][j][z] == "X":
                    stop = [i, j, z]

    return start, stop


def path_3d(p, v_start, v_stop, n):
    path = []

    w = v_stop
    x, y, z = v_to_xyz(w, n)
    path.insert(0, [x, y, z])
    while w != v_start:
        x, y, z = v_to_xyz(p[w], n)
        path.insert(0, [x, y, z])
        w = p[w]
    return path
