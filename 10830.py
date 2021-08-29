import sys

N, B = map(int, sys.stdin.readline().split())

M = [list(map(int, sys.stdin.readline().split())) for i in range(N)]


def power(M, B):
    if B == 1:
        for i in range(len(M)):
            for j in range(len(M)):
                M[i][j] %= 1000
        return M
    else:
        temp = power(M, B // 2)
        if B % 2 == 0:
            return multi(temp, temp)
        else:
            return multi(multi(temp, temp), M)


def multi(a, b):
    result = [[0] * len(a) for i in range(len(a))]
    for i in range(len(a)):
        for j in range(len(a)):
            sum = 0
            for n in range(len(a)):
                sum += a[i][n] * b[n][j]
            result[i][j] = sum % 1000

    return result


result = power(M, B)
for l in result:
    print(*l)
