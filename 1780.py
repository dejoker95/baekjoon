import sys

N = int(sys.stdin.readline())

m = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


zero_cnt = 0
one_cnt = 0
minus_cnt = 0


def check(M, length, i, j):
    cur = M[i][j]
    for row in range(i, i + length):
        for col in range(j, j + length):
            if cur != M[row][col]:
                return False
    return True


def solve(M, length, i, j):
    global zero_cnt, one_cnt, minus_cnt

    if check(M, length, i, j):
        if M[i][j] == 0:
            zero_cnt += 1
        elif M[i][j] == 1:
            one_cnt += 1
        else:
            minus_cnt += 1
    else:
        third = length // 3
        for r in range(3):
            for c in range(3):
                solve(M, third, i + third * r, j + third * c)


solve(m, N, 0, 0)

print(minus_cnt)
print(zero_cnt)
print(one_cnt)
