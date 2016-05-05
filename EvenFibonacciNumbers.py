T = int(input())
while T > 0:
    N = int(input())
    a, b = 0, 2
    total = 0
    while a < N:
        a, b = b, (a + 4 * b)
        total += a
    print(total - a)
    T -= 1

