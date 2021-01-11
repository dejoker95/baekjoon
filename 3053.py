import math
def euclidean(x):
    return x**2*math.pi

def taxi(x):
    return x**2*2

x = int(input())

print('{0:0.6f}'.format(euclidean(x)))
print('{0:0.6f}'.format(taxi(x)))