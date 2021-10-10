import sys
from collections import deque


def bfs(graph, visited):
    global N, M
    queue = deque()
    queue.append((0, 0, 1))
    visited[0][0][1] = 1

    nx = [-1, 1, 0, 0]
    ny = [0, 0, -1, 1]

    while queue:
        i, j, wall = queue.popleft()

        if i == N - 1 and j == M - 1:
            return visited[i][j][wall]

        for x, y in zip(nx, ny):
            ni = i + x
            nj = j + y
            if 0 <= ni < N and 0 <= nj < M:
                if graph[ni][nj] == 1 and wall == 1:
                    visited[ni][nj][0] = visited[i][j][1] + 1
                    queue.append((ni, nj, 0))
                elif graph[ni][nj] == 0 and visited[ni][nj][wall] == 0:
                    visited[ni][nj][wall] = visited[i][j][wall] + 1
                    queue.append((ni, nj, wall))
    return -1


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    graph = [list(map(int, list(read().strip()))) for _ in range(N)]
    visited = [[[0] * 2 for _ in range(M)] for _ in range(N)]
    print(bfs(graph, visited))