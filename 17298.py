N = int(input())
nums = list(map(int, input().split()))
ans = [-1] * N
stack = [0]


for i in range(1, N):
    while stack and nums[stack[-1]] < nums[i]:
        ans[stack.pop()] = nums[i]
    stack.append(i)

print(*ans)
