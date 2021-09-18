import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    P = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

    P.sort()
    Max = P[0][1]
    ans = 1
    for i in range(1, len(P)):
        if Max > P[i][1]:
            ans += 1
            Max = P[i][1]
    print(ans)
