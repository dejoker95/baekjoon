import sys
from collections import deque

N = int(sys.stdin.readline())
d = deque([])

for _ in range(N):
    s = sys.stdin.readline().split()

    if s[0] == "push_front":
        d.appendleft(s[1])
    elif s[0] == "push_back":
        d.append(s[1])
    elif s[0] == "pop_front":
        if len(d) > 0:
            print(d.popleft())
        else:
            print(-1)
    elif s[0] == "pop_back":
        if len(d) > 0:
            print(d.pop())
        else:
            print(-1)
    elif s[0] == "size":
        print(len(d))
    elif s[0] == "empty":
        if len(d):
            print(0)
        else:
            print(1)
    elif s[0] == "front":
        if len(d) > 0:
            print(d[0])
        else:
            print(-1)
    elif s[0] == "back":
        if len(d) > 0:
            print(d[-1])
        else:
            print(-1)