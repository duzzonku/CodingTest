from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(r, c):
    queue = deque([(r, c)])
    visited[r][c] = True
    count = 1

    while queue:
        cur_r, cur_c= queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if board[nr][nc] == 1:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
                        count += 1
            
    return count


N = int(input())
board = [list(map(int, input())) for _ in range(N)]
visited = [[False]*N for _ in range(N+1)]
house_list = []

for i in range(N):
    for j in range(N):
        if board[i][j] == 1:
            if not visited[i][j]:
                cnt = bfs(i, j)
                house_list.append(cnt)

house_list.sort()

print(len(house_list))

for x in house_list:
    print(x)