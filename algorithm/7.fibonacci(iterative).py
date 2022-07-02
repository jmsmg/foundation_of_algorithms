# n = int(input())

# a = 1
# b = 1
# if n == 1 or n == 2:
#     print(1)
# else:
#     for i in range(1, n):
#         a, b = b, b + a

# print(a)

n = int(input())

f = [0] * (n+1)
if (n > 0):
    f[1] = 1
    for i in range(2, n+1):
        f[i] = f[i - 1] + f[i - 2]

print(f[n])