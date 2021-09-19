S = list(input().strip())
T = list(input().strip())

while True:
    if len(T) == len(S):
        for i in range(len(T)):
            if T[i] != S[i]:
                print(0)
                exit()
        print(1)
        exit()

    if T[-1] == "A":
        T = T[:-1]
    else:
        T = T[:-1]
        T.reverse()