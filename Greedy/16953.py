import sys
from collections import deque

A, B = map(int, sys.stdin.readline().split())

# ans = -1
# Q = deque([(A, 1)])

# while Q:
#     i, cnt = Q.popleft()

#     if i == B:
#         ans = cnt
#         break
#     if i * 2 <= B:
#         Q.append((i * 2, cnt + 1))
#     if 10 * i + 1 <= B:
#         Q.append((10 * i + 1, cnt + 1))
# print(ans)


cnt = 1
while True:
    if A == B:
        break
    elif (B % 2 != 0 and B % 10 != 1) or (B < A):
        cnt = -1
        break
    else:
        if B % 10 == 1:
            B //= 10
        else:
            B //= 2
        cnt += 1
print(cnt)