import sys


def in_circle(x, y, a, b, r):
    if (x - a) ** 2 + (y - b) ** 2 > r ** 2:
        return 0
    else:
        return 1


T = int(sys.stdin.readline())

for _ in range(T):
    x1, y1, x2, y2 = map(int, sys.stdin.readline().split())
    N = int(sys.stdin.readline())
    count = 0
    for i in range(N):
        a, b, r = map(int, sys.stdin.readline().split())
        if in_circle(x1, y1, a, b, r) + in_circle(x2, y2, a, b, r) == 1:
            count += 1
    print(count)
