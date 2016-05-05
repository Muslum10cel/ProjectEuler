T = int(input())
while T > 0:
    N = int(input())
    x = (N * (N + 1)) // 2
    y = (N * (N + 1) * (2 * N + 1)) // 6
    print((x ** 2) - y)
    T -= 1
