from collections import deque

N, K = map(int, input().split())

q = deque([i for i in range(1, N + 1)])
ans = []

cnt = 1
while q:
    if cnt == K:
        ans.append(q.popleft())
        cnt = 1
    else:
        a = q.popleft()
        q.append(a)
        cnt += 1
print("<" + str(ans)[1:-1] + ">")
