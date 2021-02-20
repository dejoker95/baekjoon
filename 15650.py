import sys

n, m = map(int, sys.stdin.readline().split())

visited = [0 for i in range(n)]
arr = []

def dfs(cnt):
    if cnt == m:
        print(*arr)
        return
    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            arr.append(i+1)
            dfs(cnt+1)
            arr.pop()
            for j in range(i+1, n):
                visited[j] = 0

dfs(0)


"""
from itertools import combinations
n, m = map(int, sys.stdin.readline().split())
p = combinations(range(1, n+1), m)
for i in p:
    print(*i)

"""