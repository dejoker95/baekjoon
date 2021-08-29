import sys

N = int(sys.stdin.readline())

m = [list(map(int, sys.stdin.readline().split())) for i in range(N)]

white_cnt = 0
blue_cnt = 0


def check(M, length, i, j):
    cur = M[i][j]
    for row in range(i, i + length):
        for col in range(j, j + length):
            if cur != M[row][col]:
                return False
    return True


def solve(M, length, i, j):
    global white_cnt, blue_cnt

    if check(M, length, i, j):
        if M[i][j] == 0:
            white_cnt += 1
        else:
            blue_cnt += 1
    else:
        half = length // 2
        solve(M, half, i, j)
        solve(M, half, i + half, j)
        solve(M, half, i, j + half)
        solve(M, half, i + half, j + half)


solve(m, len(m), 0, 0)

print(white_cnt)
print(blue_cnt)