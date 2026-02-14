from collections import deque


def solve(N, M, grid):
    q = deque()
    dist = [[-1] * M for _ in range(N)]

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    for row in range(N):
        for col in range(M):
            if grid[row][col] == 'W':
                q.append((row, col))
                dist[row][col] = 0

    while q:
        r, c = q.popleft()

        for d in range(4):
            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

    total_dist = 0
    for r in range(N):
        for c in range(M):
            total_dist += dist[r][c]

    return total_dist


T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    grid = [list(input().strip()) for _ in range(N)]

    result = solve(N, M, grid)
    print(f'#{tc} {result}')
