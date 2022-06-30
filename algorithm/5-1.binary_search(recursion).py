def binary(n:int, S:list, left_idx:int, right_idx:int) -> int:

    mid_idx = (left_idx + right_idx) // 2

    if left_idx == right_idx:
        return -1
    elif S[mid_idx] < n:
        return binary(n, S, mid_idx+1, right_idx)
    elif S[mid_idx] > n:
        return binary(n, S, left_idx, mid_idx)
    else:
        return mid_idx

n = int(input())
S = list(map(int, input().split()))

left_idx = 0
right_idx = len(S)
print(binary(n, S, left_idx, right_idx))