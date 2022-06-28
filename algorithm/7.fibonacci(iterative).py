n = int(input())

a = 1
b = 1
if n == 1 or n == 2:
    print(1)
else:
    for i in range(1, n):
        a, b = b, b + a

print(a)