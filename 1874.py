N = int(input())

s = [int(input()) for _ in range(N)]

idx = s.index(N)


stack = []
ans = []
count = 1
for i in range(idx + 1):
    if len(stack) == 0 or stack[-1] < s[i]:
        while True:
            stack.append(count)
            ans.append("+")
            count += 1
            if count > s[i]:
                break
        stack.pop()
        ans.append("-")
    elif stack[-1] == s[i]:
        stack.pop()
        ans.append("-")
    elif stack[-1] > s[i]:
        if s[i] not in stack:
            print("NO")
            exit()
        while len(stack) > 0:
            if stack[-1] == s[i]:
                stack.pop()
                ans.append("-")
                break
            stack.pop()
            ans.append("-")


if idx < len(s) - 1:
    cur = s[idx]
    for i in range(idx + 1, len(s)):
        if s[i] > cur or s[i] not in stack:
            print("NO")
            exit()
        cur = s[i]
        ans.append("-")


for c in ans:
    print(c)