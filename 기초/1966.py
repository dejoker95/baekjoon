from collections import deque

N = int(input())


for _ in range(N):
    n, idx = map(int, input().split())
    priority = deque(list(map(int, input().split())))
    cnt = 1
    while True:
        if priority[0] == max(priority):
            if idx == 0:
                print(cnt)
                break
            else:
                priority.popleft()
                idx -= 1
                cnt += 1
        else:
            if idx == 0:
                a = priority.popleft()
                priority.append(a)
                idx = len(priority) - 1
            else:
                a = priority.popleft()
                priority.append(a)
                idx -= 1
