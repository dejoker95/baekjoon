import sys

N = int(sys.stdin.readline())
T = []
for _ in range(N):
    T.append(int(sys.stdin.readline()))


memo = {0: 0, 1: 1, 2: 1, 3: 1}


def P(n):
    if n in memo:
        return memo[n]
    else:
        memo[n] = P(n - 2) + P(n - 3)
        return memo[n]


for t in T:
    print(P(t))
