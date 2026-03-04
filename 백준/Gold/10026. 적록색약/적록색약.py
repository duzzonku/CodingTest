from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(r, c, color):
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
                    if picture[nr][nc] == color:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    return


N = int(input())
picture = [list(input()) for _ in range(N)]
visited = [[False] * N for _ in range(N)]


normal_cnt = 0

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, picture[i][j])
            normal_cnt += 1


visited = [[False] * N for _ in range(N)]

not_green_red_cnt = 0
for k in range(N):
    for l in range(N):
        if picture[k][l] == 'G':
            picture[k][l] = 'R'

for i in range(N):
    for j in range(N):
        if not visited[i][j]:
            bfs(i, j, picture[i][j])
            not_green_red_cnt += 1

print(f'{normal_cnt} {not_green_red_cnt}')