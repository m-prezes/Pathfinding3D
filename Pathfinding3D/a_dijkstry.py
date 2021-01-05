from utils import *


def a_dijkstry(ngb, n, v_start, v_stop, mc):
    S = []
    Q = v_in_Q(ngb)
    d = []
    p = []
    blocks = 0
    final = "Ilosc sprawdzonych blokow: "

    for i in range(n * n * n):
        d.append(1000)
        p.append(-1)

    d[v_start] = 0

    while Q != []:
        u = min_in_Q(Q, d)
        setMove(u, n, mc)
        blocks += 1
        if u == -1:
            return p, False
        Q.remove(u)
        S.append(u)
        for w in ngb[u]:
            if w not in Q:
                continue
            if d[w] > d[u] + 1:
                d[w] = d[u] + 1
                p[w] = u
            if w == v_stop:
                final += str(blocks)
                mc.postToChat(final)
                return p, True

    return p, False
