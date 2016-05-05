import math

T = int(input())
while T > 0:
    N = int(input())
    x = ((3 * math.floor((N - 1) / 3)) * (math.floor((N - 1) / 3) + 1)) // 2
    y = ((5 * math.floor((N - 1) / 5)) * (math.floor((N - 1) / 5) + 1)) // 2
    z = ((15 * math.floor((N - 1) / 15)) * (math.floor((N - 1) / 15) + 1)) // 2
    print(x+y-z)
    T -= 1
