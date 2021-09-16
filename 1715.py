import sys
import heapq

N = int(sys.stdin.readline())
h = []

for i in range(N):
    heapq.heappush(h, int(sys.stdin.readline()))

ans = 0
while len(h) > 1:
    a = heapq.heappop(h)
    b = heapq.heappop(h)
    s = a + b
    ans += s
    heapq.heappush(h, s)
print(ans)
