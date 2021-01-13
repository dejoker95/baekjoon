def check(matrix):
    count1 = 0
    count2 = 0
    for i in range(8):
        for j in range(8):
            a = (0 if i in [0, 2, 4, 6] else 1)
            b = (0 if j in [0, 2, 4, 6] else 1)
            if (a==0 and b==0) or (a==1 and b==1):
                if matrix[i][j] != 'B':
                    count1 += 1
                else:
                    count2 += 1
            if (a==0 and b==1) or (a==1 and b==0):
                if matrix[i][j] != "W":
                    count1 += 1
                else:
                    count2 += 1
    return min(count1, count2)
            

n, m = map(int, input().split())
board = [list(input()) for i in range(n)]
result = []
for i in range(n-7):
    for j in range(m-7):
        matrix = [part[j:j+8] for part in board[i:i+8]]
        result.append(check(matrix))
print(min(result))