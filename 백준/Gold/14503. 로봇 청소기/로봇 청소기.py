from collections import deque

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

def solve(r, c, d):
    cnt = 0
    while True:
        if board[r][c] == 0:
            cnt += 1
            board[r][c] = -1

        find_empty = False
        
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    find_empty = True
                    break

        if find_empty:
            d = (d + 3) % 4

            nr = r + dr[d]
            nc = c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 0:
                    r, c = nr, nc

        else:
            br = r - dr[d]
            bc = c - dc[d]

            if 0 <= br < N and 0 <= bc < M:
                if board[br][bc] != 1:
                    r, c = br, bc
            
                else:
                    return cnt
            else:
                return cnt


N, M = map(int, input().split())
robot_r, robot_c, robot_d = list(map(int, input().split()))
board = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N+1)]

result = solve(robot_r, robot_c, robot_d)
print(result)