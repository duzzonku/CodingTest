from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]

def bfs(start_r, start_c, end_r, end_c, k1):
    queue = deque([(start_r, start_c, 0)])
    visited[start_r][start_c] = 1

    while queue:
        cur_r, cur_c, time= queue.popleft()

        if cur_r == end_r and cur_c == end_c:
            return time

        for d in range(4):
            for k in range(1, k1+1):
                nr = cur_r + dr[d] * k
                nc = cur_c + dc[d] * k

                if not (0 <= nr < N and 0 <= nc < M):
                    break
                
                if board[nr][nc] == '#':
                    break

                if visited[nr][nc] != 0 and visited[nr][nc] < time + 1:
                    break
                            
                if visited[nr][nc] == 0:
                    visited[nr][nc] = time + 1
                    queue.append((nr, nc, time + 1))

    return -1



N, M, K = list(map(int, input().split()))
board = [list(input()) for _ in range(N)]
x1, y1, x2, y2 = list(map(int, input().split()))

visited = [[0] * M for _ in range(N+1)]

result = bfs(x1-1, y1-1, x2-1, y2-1, K)
print(result)