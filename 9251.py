str1 = input()
str2 = input()

str1 = " " + str1
str2 = " " + str2

M = [[0 for i in range(len(str1))] for i in range(len(str2))]


for i in range(1, len(M)):
    for j in range(1, len(M[0])):
        if str2[i] == str1[j]:
            M[i][j] = M[i - 1][j - 1] + 1
        else:
            M[i][j] = max(M[i][j - 1], M[i - 1][j])

print(M[-1][-1])