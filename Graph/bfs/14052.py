import sys
import copy


def spread_virus(i, j, G):
    global N, M
    if G[i][j] == 2:
        nx = [-1, 1, 0, 0]
        ny = [0, 0, -1, 1]

        for x, y in zip(nx, ny):
            ni = i + x
            nj = j + y
            if 0 <= ni < N and 0 <= nj < M:
                if G[ni][nj] == 0:
                    G[ni][nj] = 2
                    spread_virus(ni, nj, G)


def make_wall(start, cnt):
    global graph, ans
    if cnt == 3:
        G = copy.deepcopy(graph)
        for v in virus:
            i, j = v
            spread_virus(i, j, G)
        sub_ans = sum(row.count(0) for row in G)
        ans = max(ans, sub_ans)
        return
    for num in range(start, N * M):
        i = num // M
        j = num % M
        if graph[i][j] == 0:
            graph[i][j] = 1
            make_wall(num, cnt + 1)
            graph[i][j] = 0


if __name__ == "__main__":
    read = sys.stdin.readline
    N, M = map(int, read().split())
    graph = [list(map(int, read().split())) for _ in range(N)]
    virus = []
    for i in range(N):
        for j in range(M):
            if graph[i][j] == 2:
                virus.append((i, j))
    ans = -1
    make_wall(0, 0)
    print(ans)
