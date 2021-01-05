import sys
import time
import mcpi.minecraft as minecraft
import mcpi.block as block

from maze import *
from utils import plac, path_3d, xyz_to_v, ngb_from_maze, find_start_stop
from test import testIfValid

from a_dijkstry import a_dijkstry
from a_A import a_A

mc = minecraft.Minecraft.create()


def main(args):
    """
    --- Variables ---
    """
    N = 20

    """
    --- InitMaze ---
    """
    # maze = createMaze3d(N, 0.5)
    maze = exampleMaze3dRods(N, 0.2)
    # maze = test(N,0)
    plac(-5, -5, -5, N + 10, mc)
    setMaze(maze, N, mc)
    time.sleep(5)

    """
    --- Preparation start and stop ---
    """
    start, stop = find_start_stop(maze, N)
    print(start, stop)
    v_start = xyz_to_v(start[0], start[1], start[2], N)
    v_stop = xyz_to_v(stop[0], stop[1], stop[2], N)


    """
    --- Preparation neighbors ---
    """
    ngb = ngb_from_maze(maze, N)

    """
    --- Start algorithm ---
    """
    p, found = a_A(ngb, N, v_start, v_stop, mc)
    # p, found = a_dijkstry(ngb, N, v_start, v_stop, mc)




    """
    --- Write result ---
    """

    if found:
        setMaze(maze, N, mc)
        pth = path_3d(p, v_start, v_stop, N)
        print(pth)

        if testIfValid(pth, maze, start, stop):
            print("Sciezka poprawna")
            steps = "dlugosc trasy: "
            steps += str(len(pth))
            mc.postToChat(steps)
            for xyz in pth:
                mc.setBlock(xyz[1], xyz[2], xyz[0], block.OBSIDIAN)
        else:
            print("Sciezka niepoprawna")

    else:
        print("Brak drogi")

    mc.setBlock(stop[1], stop[2], stop[0], 133)
    mc.setBlock(start[1], start[2], start[0], block.DIAMOND_BLOCK)


    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
