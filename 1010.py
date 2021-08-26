N = int(input())

dp = [0 for i in range(31)]
dp[0] = 1
dp[1] = 1

for i in range(2, len(dp)):
    dp[i] = dp[i - 1] * i


for i in range(N):
    k, n = map(int, input().split())
    ans = dp[n] // (dp[n - k] * dp[k])
    print(ans)