a, b, c = map(int, input().split())


def solve(a, b, c):
    if b == 1:
        return a % c

    else:
        result = solve(a, b // 2, c)
        if b % 2 == 0:
            return result * result % c
        else:
            return result * result * a % c


print(solve(a, b, c))