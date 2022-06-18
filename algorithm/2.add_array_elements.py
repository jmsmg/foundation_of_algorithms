import sys
n = int(input('n을 입력하세요'))
S = list(map(int, sys.stdin.readline('S를 입력하세요').split()))
answer = 0

for i in S:
    answer += i

print(answer)