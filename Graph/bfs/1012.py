import sys
from collections import deque


def bfs(graph, visited, start):
    i, j = start
    queue = deque()
    queue.append((i, j))
    visited[i][j] = 1
    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]
    while queue:
        i, j = queue.popleft()

        for x, y in zip(nx, ny):
            ni = i + x
            nj = j + y
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == 1 and visited[ni][nj] == 0:
                    queue.append((ni, nj))
                    visited[ni][nj] = 1


if __name__ == "__main__":
    read = sys.stdin.readline
    T = int(read())

    for _ in range(T):
        M, N, K = map(int, read().split())
        visited = [[0] * M for _ in range(N)]
        graph = [[0] * M for _ in range(N)]

        for _ in range(K):
            x, y = map(int, read().split())
            graph[y][x] = 1

        cnt = 0
        for i in range(N):
            for j in range(M):
                if graph[i][j] == 1 and visited[i][j] == 0:
                    bfs(graph, visited, (i, j))
                    cnt += 1
        print(cnt)
