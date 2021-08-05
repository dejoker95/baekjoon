import sys

N = int(sys.stdin.readline())

memo = [0, 1, 2]


def fib(n):
    length = len(memo)
    if n < length:
        return memo[n]
    else:
        for i in range(n - length + 1):
            memo.append((memo[-1] + memo[-2]) % 15746)
        return memo[n]


print(fib(N))

"""
1
00 11
001 100 111
0000 0011 1100 1001 1111
00001 10000 10011 00111 11100 11001 11111 00100

1 2 3 5 8
"""