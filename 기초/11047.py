N, K = map(int, input().split())

coins = []
for i in range(N):
    coins.append(int(input()))

count = 0
while K > 0:
    for i in range(N):
        if i == N - 1:
            count += K // coins[i]
            K %= coins[i]
        elif coins[i] <= K and coins[i + 1] > K:
            count += K // coins[i]
            K %= coins[i]
            break

print(count)