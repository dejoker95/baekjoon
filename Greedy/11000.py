import sys
import heapq

N = int(sys.stdin.readline())

time = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

time.sort(key=lambda x: x[0])

heap = []
heapq.heappush(heap, time[0][1])

for i in range(1, N):
    if heap[0] > time[i][0]:
        heapq.heappush(heap, time[i][1])
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, time[i][1])

print(len(heap))