from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        if maze[cur_r][cur_c] == 3:
            return 1

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < 16 and 0 <= nc < 16:
                if not visited[nr][nc]:
                    if maze[nr][nc] != 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc))

    return 0


for tc in range(10):
    n = int(input())
    maze = [list(map(int, input())) for _ in range(16)]
    visited = [[False] * 16 for _ in range(16)]

    for row in range(16):
        for col in range(16):
            if maze[row][col] == 2:
                start_r, start_c = row, col

    result = bfs(start_r, start_c)
    print(f'#{tc+1} {result}')