import sys

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())


start = 1
end = k
ans = 0

while start <= end:
    mid = (start + end) // 2

    count = 0
    for i in range(1, n + 1):
        count += min(mid // i, n)

    if count < k:
        start = mid + 1
    else:
        ans = mid
        end = mid - 1

print(ans)