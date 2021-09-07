N, K = map(int, input().split())

things = []

for i in range(N):
    things.append(list(map(int, input().split())))

M = [[0 for i in range(K + 1)] for i in range(N + 1)]

for i in range(1, N + 1):
    thing = things[i - 1]
    for j in range(K + 1):
        if j >= thing[0]:
            M[i][j] = max(M[i - 1][j], M[i][j - 1], M[i - 1][j - thing[0]] + thing[1])
        else:
            M[i][j] = max(M[i - 1][j], M[i][j - 1])

print(M[-1][-1])
