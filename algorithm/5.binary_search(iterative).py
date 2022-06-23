# 원소 n개인 정렬된 배열 S에서 원소 x를 찾으세요

from xml.dom import minidom


n = int(input('리스트 원소의 갯수를 입력하세요. '))
S = list(map(int, input('리스트 S를 입력하세요. ').split()))
x = int(input('찾고자 하는 x를 입력하세요. '))

L = 0
R = n
answer = 0

while L <= R and answer == 0:
    mid = (L + R) // 2
    if (x == S[mid]):
        answer = mid
    elif (x < S[mid]):
        R = mid
    else:
        L = mid + 1
print(answer)