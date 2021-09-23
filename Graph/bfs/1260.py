from collections import deque


def dfs(graph, node):
    visited[node] = 1
    print(node, end=" ")
    for i in range(1, N + 1):
        if visited[i] == 0 and graph[node][i] == 1:
            dfs(graph, i)


def bfs(graph, node):
    queue = deque()
    queue.append(node)
    visited[node] = 1
    while queue:
        node = queue.popleft()
        print(node, end=" ")
        for i in range(1, N + 1):
            if visited[i] == 0 and graph[node][i] == 1:
                queue.append(i)
                visited[i] = 1


if __name__ == "__main__":
    N, M, V = map(int, input().split())
    graph = [[0] * (N + 1) for _ in range(N + 1)]

    for i in range(M):
        a, b = map(int, input().split())
        graph[a][b] = 1
        graph[b][a] = 1

    visited = [0] * (N + 1)
    dfs(graph, V)
    print()
    visited = [0] * (N + 1)
    bfs(graph, V)
