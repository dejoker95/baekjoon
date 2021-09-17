import sys
import heapq

N, M = map(int, sys.stdin.readline().split())

num = list(map(int, sys.stdin.readline().split()))

heap = []

for i in range(len(num)):
    heapq.heappush(heap, num[i])

for _ in range(M):
    a = heapq.heappop(heap)
    b = heapq.heappop(heap)
    for i in range(2):
        heapq.heappush(heap, a + b)

print(sum(heap))