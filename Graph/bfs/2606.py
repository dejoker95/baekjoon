import sys
from collections import deque, defaultdict

read = sys.stdin.readline

N = int(read())
M = int(read())

link = defaultdict(list)

for _ in range(M):
    a, b = map(int, read().split())
    link[a].append(b)
    link[b].append(a)


def bfs(node):
    visited = [0] * (N + 1)
    visited[1] = 1
    queue = deque()
    queue.append(node)
    cnt = -1
    while queue:
        node = queue.popleft()
        cnt += 1
        # print("node:", node, "cnt:", cnt)
        for n in link[node]:
            if visited[n] == 0:
                visited[n] = 1
                queue.append(n)
    return cnt


print(bfs(1))