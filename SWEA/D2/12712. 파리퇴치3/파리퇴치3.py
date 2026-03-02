dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

dr_cross = [-1, 1, 1, -1]
dc_cross = [1, 1, -1, -1]

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    board = [list(map(int, input().split())) for _ in range(N)]

    max_flies = 0
    for row in range(N):
        for col in range(N):
            flies = board[row][col]
            cur_r, cur_c = row, col

            for d in range(4):
                for k in range(1, M):
                    nr = cur_r + dr[d] * k
                    nc = cur_c + dc[d] * k

                    if 0 <= nr < N and 0 <= nc < N:
                        flies += board[nr][nc]

            flies_cross = board[row][col]
            cur_r, cur_c = row, col

            for d in range(4):
                for k in range(1, M):
                    nr = cur_r + dr_cross[d] * k
                    nc = cur_c + dc_cross[d] * k

                    if 0 <= nr < N and 0 <= nc < N:
                        flies_cross += board[nr][nc]

            result = max(flies, flies_cross)

            if result > max_flies:
                max_flies = result

    print(f'#{tc} {max_flies}')