from collections import deque

dr = [-1, -2, -2, -1, 1, 2, 2, 1]
dc = [2, 1, -1, -2, -2, -1, 1, 2]

def bfs(r, c, end_row, end_col):
    if r == end_row and c == end_col:
        return 0
        
    queue = deque([(r, c, 0)])
    visited[r][c] = True

    while queue:
        cur_r, cur_c, cnt = queue.popleft()

        if cur_r == end_row and cur_c == end_col:
            return cnt

        for d in range(8):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < l and 0 <= nc < l:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    queue.append((nr, nc, cnt + 1))


    return cnt

n = int(input())

for _ in range(n):
    l = int(input())
    start_r, start_c = map(int, input().split())
    end_r, end_c = map(int, input().split())

    visited = [[False]*l for _ in range(l+1)]

    result = bfs(start_r, start_c, end_r, end_c)
    print(result)