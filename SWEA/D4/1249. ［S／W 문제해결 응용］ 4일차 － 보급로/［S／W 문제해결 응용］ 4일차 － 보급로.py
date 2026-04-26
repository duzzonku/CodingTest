dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def dijkstra(r, c):
    queue = []
    queue.append((r, c))

    dist = [[float('inf')] * N for _ in range(N)]
    dist[r][c] = 0

    while queue:
        cur_r, cur_c = queue.pop(0)

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                cost = board[nr][nc] + dist[cur_r][cur_c]
                if cost < dist[nr][nc]:
                    dist[nr][nc] = cost
                    queue.append((nr, nc))

    return dist[N - 1][N - 1]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]

    ans = dijkstra(0, 0)
    print(f'#{tc} {ans}')