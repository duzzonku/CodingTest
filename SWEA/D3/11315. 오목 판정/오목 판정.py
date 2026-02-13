T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    dr_cross = [-1, -1, 1, 1]
    dc_cross = [1, -1, -1, 1]

    ans = 0

    for row in range(N):
        for col in range(N):
            if arr[row][col] == 'o':
                for d in range(4):
                    cnt = 1
                    for k in range(1, 5):
                        nr = row + dr[d] * k
                        nc = col + dc[d] * k
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                cnt += 1
                                if cnt == 5:
                                    ans += 1
                            else:
                                cnt = 0

                    cnt = 1
                    for k in range(1, 5):
                        nr = row + dr_cross[d] * k
                        nc = col + dc_cross[d] * k
                        if 0 <= nr < N and 0 <= nc < N:
                            if arr[nr][nc] == 'o':
                                cnt += 1
                                if cnt == 5:
                                    ans += 1
                            else:
                                cnt = 0
    if ans != 0:
        print(f'#{tc} YES')
    else:
        print(f'#{tc} NO')