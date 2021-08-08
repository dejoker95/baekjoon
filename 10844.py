N = int(input())


def mine(N):
    memo = [1 for i in range(10)]
    memo[0] = 0

    for i in range(1, N):
        copy = memo[:]
        for j in range(10):
            if j == 0:
                memo[j] = copy[1]
            elif j == 9:
                memo[j] = copy[8]
            else:
                memo[j] = copy[j - 1] + copy[j + 1]

    return sum(memo) % 1000000000


print(mine(N))


"""
0:0 1:1 2:1 3:1 4:1 5:1 6:1 7:1 8:1 9:1     9
0:1 1:1 2:2 3:2 4:2 5:2 6:2 7:2 8:2 9:1     17
0:1 1:3 2:3 3:4 4:4 5:4 6:4 7:4 8:3 9:2     32
0:3 1:6 2:7 3:8 4:8 5:8 6:8 7:7 8:5 9:3
"""