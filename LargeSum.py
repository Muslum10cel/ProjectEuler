testCase = int(input())
sum = 0
while testCase > 0:
    sum += int(input().strip())
    testCase -= 1
result = str(sum)
print(result[:10])