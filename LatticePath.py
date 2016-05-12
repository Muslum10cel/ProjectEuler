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
    N_M = input().split(" ")
    X = fact(int(N_M[0]) + int(N_M[1]))
    Y = fact(int(N_M[0]))
    Z = fact(int(N_M[1]))
    print((X // (Y * Z)) % ((10 ** 9) + 7))
    T -= 1
