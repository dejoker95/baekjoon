N = int(input())
nums = []
for i in range(N):
    nums.append(list(map(int, input().split())))

nums = list(sorted(nums))


dp = [0 for i in range(N)]

for i in range(N):
    for j in range(i):
        if nums[i][1] > nums[j][1] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(N - max(dp))
