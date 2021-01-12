from itertools import combinations

n, m = map(int, input().split())
card_list = list(map(int, input().split()))

result = 0

for cards in combinations(card_list, 3):
    temp = sum(cards)
    if (result < temp) and (temp <= m):
        result = temp
print(result)
