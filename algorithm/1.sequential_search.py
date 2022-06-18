# 원소가 n개인 배열 S에 원소 x가 있는가?
# 입력 정수 n, 배열 S, 원소 x
# 출력 원소 x가 위치한 인덱스를 출력 (S안에 있으면 인덱스, 없으면 0)

n = int(input('리스트 정수의 개수를 입력하세요'))
S = list(map(int, input('리스트를 만드세요').split()))
x = int(input('찾을 값을 입력하세요'))
i = 0

while S[i] != x and i <= n:
    i += 1

if i > n:
    i = 0
print(i)