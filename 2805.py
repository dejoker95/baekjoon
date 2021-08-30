import sys

N, M = map(int, sys.stdin.readline().split())
tree = list(map(int, sys.stdin.readline().split()))


start = 0
end = max(tree) - 1

while start <= end:
    mid = (start + end) // 2
    get = sum(i - mid if i > mid else 0 for i in tree)
    if get < M:
        end = mid - 1
    else:
        start = mid + 1

print(end)
