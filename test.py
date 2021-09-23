import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))
ans = [-1] * N
stack = [0]

for i in range(1, N):
    while stack and A[stack[-1]] < A[i]:
        ans[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)

print(*ans)
