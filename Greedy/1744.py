import sys
import heapq

N = int(sys.stdin.readline())

heap_pos = []
heap_neg = []
for i in range(N):
    n = int(sys.stdin.readline())
    if n > 0:
        heapq.heappush(heap_pos, -n)
    else:
        heapq.heappush(heap_neg, n)

ans = 0

while len(heap_pos) >= 2:
    a = -heapq.heappop(heap_pos)
    b = -heapq.heappop(heap_pos)
    if a == 1 or b == 1:
        ans += a + b
    else:
        ans += a * b

if len(heap_pos) == 1:
    ans += -heapq.heappop(heap_pos)

while len(heap_neg) >= 2:
    a = heapq.heappop(heap_neg)
    b = heapq.heappop(heap_neg)
    ans += a * b

if len(heap_neg) == 1:
    ans += heapq.heappop(heap_neg)

print(ans)
