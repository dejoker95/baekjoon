import sys

n = int(sys.stdin.readline())


def mat_mul(a, b):
    result = [[0] * 2 for i in range(2)]
    for i in range(2):
        for j in range(2):
            for k in range(2):
                result[i][j] += a[i][k] * b[k][j]
            result[i][j] %= 1000000007
    return result


base = [[1, 1], [1, 0]]
M = [[1, 1], [1, 0]]

if n <= 2:
    print(1)
else:
    n = n - 1
    ops = []
    while n > 1:
        if n % 2 == 0:
            ops.append(0)
            n //= 2
        else:
            n -= 1
            ops.append(1)

    for i in range(len(ops) - 1, -1, -1):
        if ops[i] == 0:
            M = mat_mul(M, M)
        else:
            M = mat_mul(M, base)

    print(M[0][0])
