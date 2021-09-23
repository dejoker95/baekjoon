import sys
from collections import deque


def bfs():
    visited = [[0] * M for _ in range(N)]
    visited[0][0] = 1
    queue = deque()
    queue.append((0, 0, 1))
    while queue:
        i, j, cnt = queue.popleft()

        if i == N - 1 and j == M - 1:
            return cnt

        if i > 0:  # upper
            if board[i - 1][j] == 1 and visited[i - 1][j] == 0:
                queue.append((i - 1, j, cnt + 1))
                visited[i - 1][j] = 1
        if i < N - 1:  # lower
            if board[i + 1][j] == 1 and visited[i + 1][j] == 0:
                queue.append((i + 1, j, cnt + 1))
                visited[i + 1][j] = 1
        if j > 0:  # left
            if board[i][j - 1] == 1 and visited[i][j - 1] == 0:
                queue.append((i, j - 1, cnt + 1))
                visited[i][j - 1] = 1
        if j < M - 1:  # right
            if board[i][j + 1] == 1 and visited[i][j + 1] == 0:
                queue.append((i, j + 1, cnt + 1))
                visited[i][j + 1] = 1


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    board = [list(map(int, list(read().strip()))) for _ in range(N)]
    print(bfs())
