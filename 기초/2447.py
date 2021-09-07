def star(n):
    global base
    if n == 3:
        base[0][:3] = ['*']*3
        base[1][:3] = ['*', ' ', '*']
        base[2][:3] = ['*']*3
        return
    a = n // 3
    star(n//3)
    for i in range(3):
        for j in range(3):
            if i == 1 and j == 1:
                continue
            for k in range(a):
                base[a*i+k][a*j:a*(j+1)] = base[k][:a]

n = int(input())
base = [[" " for i in range(n)] for i in range(n)]
star(n)
for i in range(n):
    for j in range(n):
        print(base[i][j], end='')
    print()
