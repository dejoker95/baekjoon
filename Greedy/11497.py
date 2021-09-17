import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N = int(sys.stdin.readline())
    log = list(map(int, sys.stdin.readline().split()))

    log.sort()

    ans = 0

    for i in range(2, len(log)):
        ans = max(ans, abs(log[i] - log[i - 2]))

    print(ans)