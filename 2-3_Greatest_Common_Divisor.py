def computeGCD(x, y):
    while(y):
        x, y = y, x % y
    return x


x, y = map(int, input().split())
print(computeGCD(x, y))
