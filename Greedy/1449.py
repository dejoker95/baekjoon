import sys

N, L = map(int, sys.stdin.readline().split())
hole = list(map(int, sys.stdin.readline().split()))

hole.sort()

cnt = 1
start = hole[0]
for i in range(1, len(hole)):
    if hole[i] - start + 1 > L:
        cnt += 1
        start = hole[i]
print(cnt)
