from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(sr, sc, er, ec):
    queue = deque()
    queue.append((sr, sc))
    visited[sr][sc] = 0

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] > visited[cur_r][cur_c] + board[nr][nc]:
                    visited[nr][nc] = visited[cur_r][cur_c] + board[nr][nc]
                    queue.append((nr, nc))

    return visited[er][ec]


T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    board = [list(map(int, input())) for _ in range(N)]
    visited = [[99999999] * N for _ in range(N)]

    start_r, start_c = 0, 0
    end_r, end_c = N - 1, N - 1

    result = bfs(start_r, start_c, end_r, end_c)
    print(f'#{tc} {result}')