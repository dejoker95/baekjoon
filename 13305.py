N = int(input())

distance = list(map(int, input().split()))
price = list(map(int, input().split()))

total = 0
cur_price = price[0]

for i in range(N - 1):
    if cur_price > price[i]:
        cur_price = price[i]
    total += cur_price * distance[i]
print(total)