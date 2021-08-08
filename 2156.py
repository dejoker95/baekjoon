N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))

l[1] = l[0] + l[1]

for i in range(2, N):
    pass