T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    dr_cross = [-1, -1, 1, 1]
    dc_cross = [1, -1, -1, 1]

    for row in range(N):
        for col in range(N):

            sum1 = arr[row][col]
            for d in range(4):
                for k in range(1, M):
                    nr = row + dr[d] * k
                    nc = col + dc[d] * k
                    if 0 <= nr < N and 0 <= nc < N:
                        sum1 += arr[nr][nc]

            sum2 = arr[row][col]
            for d in range(4):
                for k in range(1, M):
                    nr = row + dr_cross[d] * k
                    nc = col + dc_cross[d] * k
                    if 0 <= nr < N and 0 <= nc < N:
                        sum2 += arr[nr][nc]

            if max(sum1, sum2) > max_flies:
                max_flies = max(sum1, sum2)

    print(f'#{tc} {max_flies}')