from collections import deque

dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [1, 1, 0, -1, -1, -1, 0, 1]

def bfs(start_r, start_c):
    queue = deque()
    queue.append((start_r, start_c))
    board[start_r][start_c] = 0
    
    # 방문했던 섬 0 처리
    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(8):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < h and 0 <= nc < w:
                if board[nr][nc] == 1:
                    board[nr][nc] = 0
                    queue.append((nr, nc))
    return


while True:
    w, h = map(int, input().split())
    
    if w == 0 and h == 0:
        break
    
    board = [list(map(int, input().split())) for _ in range(h)]

    island_count = 0

    for i in range(h):
        for j in range(w):
            if board[i][j]==1:
                bfs(i, j)
                island_count += 1

    print(island_count)
