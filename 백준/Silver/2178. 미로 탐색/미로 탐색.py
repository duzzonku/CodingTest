from collections import deque

def bfs(r, c):
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    queue = deque()
    queue.append((r, c))

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if maze[nr][nc] == 1:
                    maze[nr][nc] = maze[cur_r][cur_c] + 1
                    queue.append((nr, nc))
    
    return maze[N-1][M-1]


N, M = map(int, input().split())
maze = [list(map(int, input())) for _ in range(N)]
result = bfs(0, 0)
print(result)