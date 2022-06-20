import sys

n = int(sys.stdin.readline())
S = list(map(int, sys.stdin.readline().split()))

for i in range(n):
    for j in range(n-1):
        if S[i] <= S[j]:
            S[i], S[j] = S[j], S[i]

print(S)