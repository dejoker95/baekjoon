import sys

# N = int(sys.stdin.readline())
N = 8
count = 0
board = [0 for i in range(N)]

def check(cnt):
    if cnt == 0:
        return True
    else:
        for i in range(cnt):
            if (board[i] == board[cnt]) or (abs(board[i] - board[cnt]) == abs(cnt - i)):
                return False
        return True


def dfs(cnt):
    global count
    if cnt == N:
        count += 1
        return
    for i in range(N):
        board[cnt] = i
        if check(cnt):
            dfs(cnt+1)
        

dfs(0)
print(count)