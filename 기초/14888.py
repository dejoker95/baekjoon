import sys
import math

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))
add, minus, multi, div = map(int, sys.stdin.readline().split())

max_val = -math.inf
min_val = math.inf


def solve(cnt, add, minus, multi, div, result):
    global N, max_val, min_val

    if cnt == N - 1:
        max_val = max(result, max_val)
        min_val = min(result, min_val)
        return

    if add > 0:
        solve(cnt + 1, add - 1, minus, multi, div, result + nums[cnt + 1])
    if minus > 0:
        solve(cnt + 1, add, minus - 1, multi, div, result - nums[cnt + 1])
    if multi > 0:
        solve(cnt + 1, add, minus, multi - 1, div, result * nums[cnt + 1])
    if div > 0:
        r = result // nums[cnt + 1] if result > 0 else -(-result // nums[cnt + 1])
        solve(cnt + 1, add, minus, multi, div - 1, r)


solve(0, add, minus, multi, div, nums[0])
print(max_val)
print(min_val)