import sys
from collections import defaultdict

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
D = defaultdict(list)
d = []
for _ in range(M):
    From, To, Q = map(int, sys.stdin.readline().split())
    D[From].append([To, Q])
    d.append([From, To, Q])
d.sort(key=lambda x: (x[1] - x[0], x[0]))
print("d:", d)
train = defaultdict(int)
taken = 0
ans = 0
for i in range(1, M + 1):
    if train[i] > 0:
        taken -= train[i]
        ans += train[i]
        train[i] = 0
    boxList = sorted(D[i], key=lambda x: x[0])
    for box in boxList:
        if taken + box[1] <= C:
            train[box[0]] += box[1]
            taken += box[1]
        else:
            train[box[0]] += C - taken
            taken = C

print(ans)