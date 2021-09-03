import sys

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for i in range(N)]

nums.sort()
print("nums:", nums)
if len(nums) == 1:
    print(0)
    exit()

ans = (len(nums) - 1) * nums[0]

for i in range(1, len(nums)):
    ans += (len(nums) - i) * nums[i]
print(ans)
