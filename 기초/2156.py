N = int(input())

l = []
for _ in range(N):
    l.append(int(input()))
memo = [0 for i in range(N)]

for i in range(0, N):
    if i == 0:
        memo[i] = l[i]
    elif i == 1:
        memo[i] = l[i - 1] + l[i]
    else:
        memo[i] = max(memo[i - 1], memo[i - 3] + l[i - 1] + l[i], memo[i - 2] + l[i])

print(memo[-1])