import sys
import heapq

n = int(sys.stdin.readline())
k = int(sys.stdin.readline())


def answer(n, k):
    l = []
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            l.append(i * j)
    l = list(sorted(l))
    print(l)
    return l[k]


def countPow(num):
    global n
    if num == 1:
        return 1
    elif n == num:
        return n ** 2
    return num ** 2 + (num - 1) * 2


def get_nums(mid, gap):
    global n
    heap = []
    i = mid + 1
    j = mid
    while i <= n and j >= 1:
        heapq.heappush(heap, i * j)
        i += 1
        j -= 1
    i = mid + 2
    j = mid
    while i <= n and j >= 1:
        heapq.heappush(heap, i * j)
        i += 1
        j -= 1
    ans = 0

    for i in range(gap):
        ans = heapq.heappop(heap)
    return ans


start = 1
end = n
new_k = k + 1
print("my answer:")
while start <= end:
    mid = (start + end) // 2

    count = countPow(mid)
    count_plus = countPow(mid + 1)
    if count == k + 1:
        print("count", count)
        print(mid ** 2)
        break
    elif count < k + 1 and k + 1 < count_plus:
        gap = k - count
        if gap % 2 == 0:
            gap //= 2
        else:
            gap = gap // 2 + 1
        print(get_nums(mid, gap))
        break
    elif count < k:
        start = mid + 1
    else:
        end = mid - 1

print("ans:", answer(n, k))
print("mid, gap:", mid, gap)
