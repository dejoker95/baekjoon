import sys

n, m = map(int, sys.stdin.readline().split())
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(1, n+1):
        if (len(arr) != 0) and (i < arr[len(arr)-1]):
            continue
        arr.append(i)
        dfs(cnt+1)
        arr.pop()

dfs(0)