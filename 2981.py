import math

N = int(input())
nums = [int(input()) for i in range(N)]
nums.sort()

subs = []
ans = list()

for i in range(1, N):
    subs.append(nums[i] - nums[i - 1])

deno = subs[0]
for i in range(1, len(subs)):
    deno = math.gcd(deno, subs[i])

for i in range(2, int(math.sqrt(deno)) + 1):
    if deno % i == 0:
        ans.append(i)
        ans.append(deno // i)
ans.append(deno)
ans = list(set(ans))
ans.sort()
print(*ans)