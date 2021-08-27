while True:
    line = input()
    if line == ".":
        break
    stack = []
    ans = ""
    for c in line:
        if c == "(":
            stack.append(c)
        elif c == "[":
            stack.append(c)
        elif c == ")":
            if len(stack) == 0 or stack[-1] != "(":
                ans = "no"
                break
            stack.pop()
        elif c == "]":
            if len(stack) == 0 or stack[-1] != "[":
                ans = "no"
                break
            stack.pop()

    if ans == "no":
        print("no")
    elif len(stack) == 0:
        print("yes")
    else:
        print("no")
