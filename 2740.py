import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

M, K = map(int, sys.stdin.readline().split())

B = [list(map(int, sys.stdin.readline().split())) for i in range(M)]

result = [[0] * K for i in range(N)]

for i in range(N):
    for j in range(K):
        sum = 0
        for n in range(M):
            sum += A[i][n] * B[n][j]
        result[i][j] = sum

for l in result:
    print(*l)