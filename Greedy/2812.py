import sys

N, K = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().strip()))

stack = []
d = K
for i in range(N):
    while d > 0 and stack:
        if stack[-1] < num[i]:
            stack.pop()
            d -= 1
        else:
            break
    stack.append(num[i])

for i in range(N - K):
    print(stack[i], end="")
