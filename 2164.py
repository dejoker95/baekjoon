from collections import deque

N = int(input())

q = deque([i for i in range(1, N + 1)])

cnt = 0
while len(q) > 1:
    if cnt % 2 == 0:
        q.popleft()
    else:
        a = q.popleft()
        q.append(a)
    cnt += 1

print(q[0])