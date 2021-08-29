import sys

while True:
    read = sys.stdin.readline()
    if read == "0":
        break
    l = list(map(int, read.split()))
