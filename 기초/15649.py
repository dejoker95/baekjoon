import sys

n, m = map(int, sys.stdin.readline().split())

num_list = [i+1 for i in range(n)]
check_list = [False] * n

arr = []

def dfs(cnt):
    if(cnt == m):
        print(*arr)
        return

    for i in range(n):
        if check_list[i]:
            continue

        check_list[i] = True
        arr.append(num_list[i])
        dfs(cnt+1)
        arr.pop()
        check_list[i] = False

dfs(0)