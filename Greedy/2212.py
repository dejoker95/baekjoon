import sys

N = int(sys.stdin.readline())
K = int(sys.stdin.readline())
sensor = list(map(int, sys.stdin.readline().split()))

sensor.sort()

if K >= N:
    print(0)
    exit()

dist = []

for i in range(1, N):
    dist.append(sensor[i] - sensor[i - 1])

dist.sort(reverse=True)
for i in range(K - 1):
    dist.pop(0)

print(sum(dist))