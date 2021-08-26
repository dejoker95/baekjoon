import math

N = int(input())

nums = list(map(int, input().split()))

total = nums[0] * 2

for i in range(1, N):
    divisor = math.gcd(total, nums[i] * 2)
    print(str(total // divisor) + "/" + str(nums[i] * 2 // divisor))
