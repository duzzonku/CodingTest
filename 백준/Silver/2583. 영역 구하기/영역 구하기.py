from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(r, c):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = True
    area = 1

    while queue:
        cur_r, cur_c= queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc]:
                    if board[nr][nc] == 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        area += 1

    return area


M, N, K = list(map(int, input().split()))
board = [[0]*N for _ in range(M)]
visited = [[False] * N for _ in range(M)]

for _ in range(K):
    x1, y1, x2, y2 = list(map(int, input().split()))

    for row in range(y1, y2):
        for col in range(x1, x2):
            board[row][col] = 1


ans = 0
area_result = []
for i in range(M):
    for j in range(N):
        if board[i][j] == 0:
            if not visited[i][j]:
                result = bfs(i, j)
                ans += 1
                area_result.append(result)

print(ans)
area_result.sort()
print(*area_result)
