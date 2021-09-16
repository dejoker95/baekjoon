import sys
import heapq

N, K = map(int, sys.stdin.readline().split())

gem = [list(map(int, sys.stdin.readline().split())) for i in range(N)]
bag = [int(sys.stdin.readline()) for i in range(K)]


gem.sort()
bag.sort()


ans = 0
temp = []
for b in bag:
    while gem and b >= gem[0][0]:
        heapq.heappush(temp, -gem[0][1])
        heapq.heappop(gem)

    if temp:
        ans += -heapq.heappop(temp)
    elif not gem:
        break
print(ans)
