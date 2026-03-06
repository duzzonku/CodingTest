from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(r, c, k):
    queue = deque()
    queue.append((r, c, 1, k))
    visited[k][r][c] = True

    while queue:
        cur_r, cur_c, dist, broken_cnt = queue.popleft()

        if cur_r == N-1 and cur_c == M-1:
            return dist

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if not visited[broken_cnt][nr][nc]:
                    if board[nr][nc] == 0:
                        visited[broken_cnt][nr][nc] = True
                        queue.append((nr, nc, dist + 1, broken_cnt))

                    else:
                        if broken_cnt < K:
                            if not visited[broken_cnt + 1][nr][nc]:
                                visited[broken_cnt + 1][nr][nc] = True
                                queue.append((nr, nc , dist + 1, broken_cnt + 1))

    return -1


N, M, K = list(map(int, input().split()))
board = [list(map(int, input())) for _ in range(N)]
visited = [[[False] * M for _ in range(N)] for _ in range(K + 1)]
result = bfs(0, 0, 0)
print(result)