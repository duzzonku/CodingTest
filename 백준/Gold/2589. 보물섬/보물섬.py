from collections import deque

def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c, 0))

    visited = [[False]*c for _ in range(r)]
    visited[start_r][start_c] = True
    
    max_cnt = 0

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    while queue:
        cur_r, cur_c, cur_d = queue.popleft()

        max_cnt = max(max_cnt, cur_d)

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < r and 0 <= nc < c:
                if not visited[nr][nc]:
                    if board[nr][nc] == 'L':
                        visited[nr][nc] = True
                        queue.append((nr, nc, cur_d + 1))

    return max_cnt


r, c = map(int, input().split())
board = [list(input()) for _ in range(r)]

total_max = 0
for i in range(r):
    for j in range(c):
        if board[i][j] == 'L':
            total_max = max(total_max, bfs(i, j))

print(total_max)