def is666(n):
    n = str(n)
    count = 0
    for i in n:
        if i == "6":
            count += 1
        else:
            count = 0
        if count == 3:
            return True
    return False

def getNum(n):
    count = 0
    num = 666
    while True:
        if is666(num):
            count += 1
        if count == n:
            return num
        num += 1
        
n = int(input())
print(getNum(n))
