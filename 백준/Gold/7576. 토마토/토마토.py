from collections import deque

queue = deque()

def bfs():

    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    cnt = 0

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if tomato[nr][nc] == 0:
                    if not visited[nr][nc]:
                        visited[nr][nc] = True
                        tomato[nr][nc] = tomato[cur_r][cur_c] + 1
                        queue.append((nr, nc))



M, N = map(int, input().split())
tomato = [list(map(int, input().split())) for _ in range(N)]

visited = [[False] * M for _ in range(N+1)]

for row in range(N):
    for col in range(M):
        if tomato[row][col] == 1:
            queue.append((row, col))

bfs()

ans = 0

for row in tomato:
    for x in row:
        if x == 0:
            print(-1)
            exit()
    ans = max(ans, max(row))

print(ans-1)
