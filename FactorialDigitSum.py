import sys


def fact(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return n * fact(n - 1)


sys.setrecursionlimit(1500)
T = int(input())
while T > 0:
    result = fact(int(input()))
    s = 0
    while result != 0:
        s += (result % 10)
        result //= 10
    print(s)
    T -= 1
