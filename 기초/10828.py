import sys

N = int(sys.stdin.readline())


s = []

for _ in range(N):
    order = sys.stdin.readline().split()

    if order[0] == "push":
        s.append(order[1])
    elif order[0] == "top":
        if len(s) == 0:
            print(-1)
        else:
            print(s[-1])
    elif order[0] == "empty":
        if len(s) == 0:
            print(1)
        else:
            print(0)
    elif order[0] == "size":
        print(len(s))
    elif order[0] == "pop":
        if len(s) == 0:
            print(-1)
        else:
            print(s.pop())