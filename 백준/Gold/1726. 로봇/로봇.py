from collections import deque

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

def change_dir(d):
    if d == 1: 
         return 0
    if d == 2: 
         return 2 
    if d == 3: 
         return 1 
    if d == 4: 
         return 3


def bfs(r, c, d):
    queue = deque()
    queue.append((r, c, d, 0))
    visited[r][c][d] = True

    while queue:
        cur_r, cur_c, cur_dir, cnt = queue.popleft()

        if cur_r == end_r - 1 and cur_c == end_c - 1 and cur_dir == change_dir(end_direction):
            return cnt

        for k in range(1, 4):
            nr = cur_r + dr[cur_dir] * k
            nc = cur_c + dc[cur_dir] * k

            if 0 <= nr < M and 0 <= nc < N:
                if board[nr][nc] == 1:
                        break
                
                if not visited[nr][nc][cur_dir]:
                    if board[nr][nc] == 0:
                        visited[nr][nc][cur_dir] = True
                        queue.append((nr, nc, cur_dir, cnt + 1))
                    
        right_dir = (cur_dir + 1) % 4
        if not visited[cur_r][cur_c][right_dir]:
             visited[cur_r][cur_c][right_dir] = True
             queue.append((cur_r, cur_c, right_dir, cnt + 1))

        left_dir = (cur_dir + 3) % 4
        if not visited[cur_r][cur_c][left_dir]:
             visited[cur_r][cur_c][left_dir] = True
             queue.append((cur_r, cur_c, left_dir, cnt + 1))



M, N = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(M)]
start_r, start_c, start_direction = list(map(int, input().split()))
end_r, end_c, end_direction = list(map(int, input().split()))
visited = [[[False] * 4 for _ in range(N)] for _ in range(M)]

result = bfs(start_r - 1, start_c - 1, change_dir(start_direction))
print(result)