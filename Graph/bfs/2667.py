import sys
from collections import deque


def bfs(start, board, visited):
    queue = deque()
    queue.append(start)
    i, j = start
    visited[i][j] = 1
    cnt = 0

    while queue:
        i, j = queue.popleft()
        cnt += 1
        if i > 0:  # upper
            if board[i - 1][j] == 1 and visited[i - 1][j] == 0:
                queue.append((i - 1, j))
                visited[i - 1][j] = 1
        if i < N - 1:  # lower
            if board[i + 1][j] == 1 and visited[i + 1][j] == 0:
                queue.append((i + 1, j))
                visited[i + 1][j] = 1
        if j > 0:  # left
            if board[i][j - 1] == 1 and visited[i][j - 1] == 0:
                queue.append((i, j - 1))
                visited[i][j - 1] = 1
        if j < N - 1:  # right
            if board[i][j + 1] == 1 and visited[i][j + 1] == 0:
                queue.append((i, j + 1))
                visited[i][j + 1] = 1
    return cnt


if __name__ == "__main__":
    read = sys.stdin.readline
    N = int(read())
    board = [list(map(int, list(read().strip()))) for _ in range(N)]
    visited = [[0] * N for _ in range(N)]
    result = []

    for i in range(N):
        for j in range(N):
            if board[i][j] == 1 and visited[i][j] == 0:
                result.append(bfs((i, j), board, visited))

    result.sort()
    print(len(result))
    for r in result:
        print(r)
