from collections import deque

dz = [1, -1, 0, 0, 0, 0]  # 위(+1), 아래(-1)
dr = [0, 0, 1, -1, 0, 0]  # 앞(+1), 뒤(-1)
dc = [0, 0, 0, 0, -1, 1]  # 왼쪽(-1), 오른쪽(+1)

M, N, H = map(int, input().split())
tomato = [[list(map(int, input().split())) for _ in range(N)] for _ in range(H)]
visited = [[[False] * M for _ in range(N)] for _ in range(H)]

queue = deque()

for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 1:
                queue.append((k, i, j))
                visited[k][i][j] = True

while queue:
    cur_z, cur_r, cur_c = queue.popleft()

    for d in range(6):
        nr = cur_r + dr[d]
        nc = cur_c + dc[d]
        nz = cur_z + dz[d]

        if 0 <= nr < N and 0 <= nc < M and 0 <= nz < H:
            if not visited[nz][nr][nc]:
                if tomato[nz][nr][nc] == 0:
                    visited[nz][nr][nc] = True
                    tomato[nz][nr][nc] = tomato[cur_z][cur_r][cur_c] + 1
                    queue.append((nz, nr, nc)) 

ans = 0
for k in range(H):
    for i in range(N):
        for j in range(M):
            if tomato[k][i][j] == 0:
                print(-1)
                exit()
            
            if tomato[k][i][j] > ans:
                ans = tomato[k][i][j]

print(ans-1)