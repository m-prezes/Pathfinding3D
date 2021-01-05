def testIfValid(path, maze, start, stop):
    if path[0] == start and path[-1] == stop:
        for i in range(len(path) - 1):
            a = path[i]
            b = path[i + 1]
            if abs(a[0] - b[0]) + abs(a[1] - b[1]) + abs(a[2] - b[2]) == 1:
                if i + 1 == len(path) - 1 and b == stop:
                    return True
                elif maze[b[0]][b[1]][b[2]] == ' ':
                    continue
            else:
                break
    return False
