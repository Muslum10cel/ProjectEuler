T = int(input())
while T > 0:
    N = int(input())
    N = 2 ** N
    N = str(N)
    s = 0
    for i in range(len(N)):
        s += int(N[i])
    print(s)
    T -= 1
