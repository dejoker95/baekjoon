N = int(input())

for _ in range(N):
    stack = []
    ans = ""
    paren = input()

    for c in paren:
        if c == "(":
            stack.append(0)
        else:
            if len(stack) == 0:
                ans = "NO"
                break
            stack.pop()

    if ans == "NO":
        print(ans)
    elif len(stack) == 0:
        print("YES")
    else:
        print("NO")
