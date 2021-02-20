import sys

n, m = map(int, sys.stdin.readline().split())

arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    
    for i in range(1, n+1):
        arr.append(i)
        dfs(cnt+1)
        arr.pop()

dfs(0)
