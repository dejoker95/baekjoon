import sys

K, N = map(int, sys.stdin.readline().split())

line = [int(sys.stdin.readline()) for i in range(K)]

start, end = 1, max(line)

while start <= end:
    mid = (start + end) // 2
    cnt = 0
    for l in line:
        cnt += l // mid

    if cnt < N:
        end = mid - 1
    else:
        start = mid + 1

print(end)
