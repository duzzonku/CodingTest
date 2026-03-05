from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(r, c, H):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if board[nr][nc] > H:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    return 


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

max_h = 0
for i in range(N):
    for j in range(N):
        if board[i][j] > max_h:
            max_h = board[i][j]

ans = 0
for h in range(max_h + 1):
    visited = [[False] * N for _ in range(N)]
    safe_area_cnt = 0

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                if board[i][j] > h:
                    bfs(i, j, h)
                    safe_area_cnt += 1
    
    if safe_area_cnt > ans:
        ans = safe_area_cnt

print(ans)