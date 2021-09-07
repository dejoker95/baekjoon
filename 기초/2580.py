import sys

# check 메서드는 0 자리에 들어갈 수 있는 후보를 리스트로 반환
def check(i, j):
    numbers = set(range(1, 10))

    # 가로 세로 검사
    for k in range(9):
        if M[i][k] in numbers:
            numbers.remove(M[i][k])
        if M[k][j] in numbers:
            numbers.remove(M[k][j])

    # box 검사
    i = i // 3
    j = j // 3
    for row in range(3 * i, 3 * (i + 1)):
        for col in range(3 * j, 3 * (j + 1)):
            if M[row][col] in numbers:
                numbers.remove(M[row][col])
    return numbers


def do_sudoku(n):
    global is_done
    if is_done == True:
        return

    if n == len(zeros_idx):
        for row in M:
            print(*row)
        is_done = True
        return
    else:
        i, j = zeros_idx[n]
        candidates = check(i, j)
        for c in candidates:
            M[i][j] = c
            do_sudoku(n + 1)
            M[i][j] = 0


M = [list(map(int, sys.stdin.readline().split())) for _ in range(9)]

zeros_idx = [(i, j) for i in range(9) for j in range(9) if M[i][j] == 0]

is_done = False

do_sudoku(0)
