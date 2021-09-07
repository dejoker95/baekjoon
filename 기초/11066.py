import sys

case = int(sys.stdin.readline())

for _ in range(case):
    N = int(sys.stdin.readline())
    page = [0] + list(map(int, sys.stdin.readline().split()))

    # S[i]는 1부터 i까지 누적합
    S = [0 for i in range(N + 1)]
    for i in range(1, N + 1):
        S[i] = S[i - 1] + page[i]

    # dp[i][j]는 i부터 j 까지 합하는데 필요한 최소비용
    # dp[i][k] + dp[k+1][j] + sum(A[i] ~ A[j])
    dp = [[0 for i in range(N + 1)] for j in range(N + 1)]
    for i in range(2, N + 1):  # 간격
        for j in range(1, N + 2 - i):  # 시작점
            minimum = min(dp[j][j + k] + dp[j + k + 1][j + i - 1] for k in range(i - 1))
            dp[j][j + i - 1] = minimum + S[j + i - 1] - S[j - 1]
    print(dp[1][N])