n, s = map(int, input().split())
arr = list(map(int, input().split()))

cnt = 0

for bit in range(1, 1 << n):
    arr_sum = 0
    for i in range(n):
        if bit & (1 << i):
            arr_sum += arr[i]

    if arr_sum == s:
        cnt += 1

print(cnt)