import sys, math

N = int(sys.stdin.readline())
score = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
min_val = math.inf


def split(cnt, g1, g2):
    global N, min_val
    if cnt == N:
        s1 = 0
        s2 = 0
        for n in g1:
            for m in g1:
                s1 += score[n][m]
        for n in g2:
            for m in g2:
                s2 += score[n][m]

        min_val = min(abs(s1 - s2), min_val)
        return

    if len(g1) < N // 2:
        split(cnt + 1, g1 + [cnt], g2)
    if len(g2) < N // 2:
        split(cnt + 1, g1, g2 + [cnt])


split(0, [], [])
print(min_val)
