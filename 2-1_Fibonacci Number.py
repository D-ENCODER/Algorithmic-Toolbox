# Uses python3
def fibonacci(n):
    Arr = [0, 1]
    for i in range(2, n+1):
        Arr.append(Arr[i-1]+Arr[i-2])
    return Arr[n]


print(fibonacci(int(input())))
