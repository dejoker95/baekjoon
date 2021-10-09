import sys
from collections import deque


def bfs(graph, visited):

    queue = deque()
    for i in range(len(graph)):
        for j in range(len(graph[0])):
            if graph[i][j][0] == 1:
                queue.append((i, j, 0))
                visited[i][j] = 1
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    while queue:
        i, j, d = queue.popleft()

        for x, y in zip(nx, ny):
            ni = i + x
            nj = j + y
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj][0] == 0 and visited[ni][nj] == 0:
                    queue.append((ni, nj, d + 1))
                    visited[ni][nj] = 1
                    graph[ni][nj][0] = 1
                    graph[ni][nj][1] = d + 1


if __name__ == "__main__":
    read = sys.stdin.readline

    M, N = map(int, read().split())

    graph = [list(map(lambda x: [int(x), 0], read().split())) for _ in range(N)]
    visited = [[0] * M for _ in range(N)]

    bfs(graph, visited)

    ans = -1
    for i in range(N):
        for j in range(M):
            if graph[i][j][0] == 0:
                print(-1)
                exit()
            ans = max(ans, graph[i][j][1])
    print(ans)