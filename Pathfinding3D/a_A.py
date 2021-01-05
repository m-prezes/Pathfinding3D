from queue import PriorityQueue
from utils import *
import math


def heuristic_euk(a, b, n):
    x1, y1, z1 = v_to_xyz(a, n)
    x2, y2, z2 = v_to_xyz(b, n)
    return math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2) + (z1 - z2) * (z1 - z2))


def a_A(ngb, n, v_start, v_stop, mc):
    Q = PriorityQueue()
    From = [-1 for _ in range(n * n * n)]
    Cost = [-1 for _ in range(n * n * n)]
    blocks = 0
    final = "Ilosc sprawdzonych blokow: "
    Q.put((0, v_start))
    Cost[v_start] = 0

    while not Q.empty():
        v = Q.get()[1]
        setMove(v, n, mc)
        blocks += 1
        if v == v_stop:
            final += str(blocks)
            mc.postToChat(final)
            return From, True

        for u in ngb[v]:
            new_cost = Cost[v] + 1
            if Cost[u] == -1 or new_cost < Cost[u]:
                Cost[u] = new_cost
                priority = new_cost + heuristic_euk(v_stop, u, n)
                Q.put((priority, u))
                From[u] = v

    return From, False
