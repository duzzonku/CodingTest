def solve(q):
    cnt = 1
    while True:
        num = q.pop(0)
        num -= cnt

        if num <= 0:
            num = 0
            q.append(num)
            return

        q.append(num)

        cnt += 1
        if cnt > 5:
            cnt = 1


for tc in range(1, 11):
    n = int(input())
    data = list(map(int, input().split()))
    solve(data)
    print(f'#{tc}', *data)
