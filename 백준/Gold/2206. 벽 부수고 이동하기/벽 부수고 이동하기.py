from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(end_r, end_c):
    queue = deque([(0, 0, 1, 0)])
    visited[0][0][0] = True

    while queue:
        cur_r, cur_c, dist, k = queue.popleft()

        if cur_r == end_r-1 and cur_c == end_c-1:
            return dist

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[k][nr][nc]:
                    if board[nr][nc] == 0:
                        visited[k][nr][nc] = True
                        queue.append((nr, nc, dist+1, k))
        
        if k < 1:
            for d in range(4):
                nr = cur_r + dr[d]
                nc = cur_c + dc[d]

                if 0 <= nr < N and 0 <= nc < M:
                    if not visited[k][nr][nc]:
                        if board[nr][nc] == 1:
                            visited[k][nr][nc] = True
                            queue.append((nr, nc, dist+1, k+1))

    return -1


N, M = map(int, input().split())
board = [list(map(int, input())) for _ in range(N)]
visited = [[[False]*M for _ in range(N)] for _ in range(2)]

result = bfs(N, M)
print(result)
