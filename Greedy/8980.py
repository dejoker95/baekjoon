import sys

N, C = map(int, sys.stdin.readline().split())
M = int(sys.stdin.readline())
D = []
temp = [C] * N

for _ in range(M):
    D.append(list(map(int, sys.stdin.readline().split())))
D.sort(key=lambda x: x[1])


ans = 0
for i in range(M):
    minNum = C + 1
    for j in range(D[i][0], D[i][1]):
        if temp[j] < minNum:
            minNum = temp[j]
    t = min(minNum, D[i][2])
    ans += t
    for j in range(D[i][0], D[i][1]):
        temp[j] -= t

print(ans)