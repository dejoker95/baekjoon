N = int(input())
nums = list(map(int, input().split()))
small = min(nums)
big = max(nums)

print(small * big)