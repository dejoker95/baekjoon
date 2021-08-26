n, k = map(int, input().split())

dp = [0 for i in range(1001)]
dp[0] = 1
dp[1] = 1


for i in range(2, len(dp)):
    dp[i] = dp[i - 1] * i


answer = dp[n] // (dp[n - k] * dp[k])
print(answer % 10007)