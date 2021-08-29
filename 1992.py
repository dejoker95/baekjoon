import sys

N = int(sys.stdin.readline())

m = [[] for i in range(N)]
for l in m:
    s = sys.stdin.readline().strip()
    for num in s:
        l.append(int(num))


def check(M, length, i, j):
    cur = M[i][j]
    for row in range(i, i + length):
        for col in range(j, j + length):
            if cur != M[row][col]:
                return False
    return True


def solve(M, length, i, j):
    global result
    if check(M, length, i, j):
        result += str(M[i][j])
    else:
        half = length // 2
        result += "("
        solve(M, half, i, j)
        solve(M, half, i, j + half)
        solve(M, half, i + half, j)
        solve(M, half, i + half, j + half)

        result += ")"


result = ""
solve(m, N, 0, 0)

print(result)