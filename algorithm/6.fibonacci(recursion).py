def fibonacci(n -> int):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n+1)

n = int(input())

print(fibonacci(n))