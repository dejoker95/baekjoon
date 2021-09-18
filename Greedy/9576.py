import sys

T = int(sys.stdin.readline())

for _ in range(T):
    N, M = map(int, sys.stdin.readline().split())
    stu = [list(map(int, sys.stdin.readline().split())) for i in range(M)]
    book = [0] * (N + 1)
    stu.sort(key=lambda x: x[1])
    count = 0
    while stu:
        a, b = stu.pop(0)
        for i in range(a, b + 1):
            if book[i] == 0:
                count += 1
                book[i] = 1
                break
    print(count)