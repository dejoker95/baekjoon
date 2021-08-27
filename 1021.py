from collections import deque

N, M = map(int, input().split())
index = list(map(int, input().split()))

cnt = 0
while len(index) > 0:
    num = index[0]
    if num - 1 <= N + 1 - num:
        cnt += num - 1
        for i in range(len(index)):
            index[i] -= num
            if index[i] < 1:
                index[i] += N
    else:
        cnt += N - num + 1
        for i in range(len(index)):
            index[i] += N - num
            if index[i] > N:
                index[i] -= N
    index.pop(0)
    N -= 1

print(cnt)
