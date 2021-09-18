import sys

N, M = map(int, sys.stdin.readline().split())

A = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]
B = [list(map(int, list(sys.stdin.readline().strip()))) for _ in range(N)]


def change(i, j):
    for row in range(i, i + 3):
        for col in range(j, j + 3):
            A[row][col] = 1 - A[row][col]


cnt = 0
for i in range(N - 2):
    for j in range(M - 2):
        if A[i][j] != B[i][j]:
            change(i, j)
            cnt += 1

for i in range(N):
    for j in range(M):
        if A[i][j] != B[i][j]:
            print(-1)
            exit()

print(cnt)
