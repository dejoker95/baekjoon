import sys
from bisect import bisect_left

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

dp = [0]

for a in A:
    if dp[-1] < a:
        dp.append(a)
    else:
        dp[bisect_left(dp, a)] = a

print(len(dp) - 1)


"""
수동 이분탐색

for a in A:
    if dp[-1] < a:
        dp.append(a)
    else:
        start = 0
        end = len(dp) - 1

        while start <= end:
            mid = (start + end) // 2

            if dp[mid] < a:
                start = mid + 1
            else:
                end = mid - 1
        
        dp[start] = a

print(len(dp) - 1)

"""
