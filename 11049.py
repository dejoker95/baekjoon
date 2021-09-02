import sys
import math

N = int(sys.stdin.readline())

M = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

dp = [[0 for i in range(N)] for j in range(N)]

for i in range(1, N):  # 간격
    for j in range(N - i):
        x = j + i
        dp[j][x] = math.inf
        for k in range(j, x):
            dp[j][x] = min(
                dp[j][x], dp[j][k] + dp[k + 1][x] + M[j][0] * M[k][1] * M[x][1]
            )

print(dp[0][-1])