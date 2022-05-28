hash = dict()

def getLCM(a, b):
    global hash
    if (a, b) in hash:
        return hash[(a, b)]
    c, d = max(a, b), min(a, b)
    while c != d:
        temp = c - d
        c, d = max(temp, d), min(temp, d)

    hash[(a, b)] = a * b // c
    return a * b // c


x, y = map(int, input().split())
print(getLCM(x, y))
