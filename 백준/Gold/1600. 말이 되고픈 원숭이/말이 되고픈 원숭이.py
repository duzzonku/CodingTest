from collections import deque

dr_monkey = [0, -1, 0, 1]
dc_monkey = [1, 0, -1, 0]

dr_horse = [-2, -2, -1, -1, 1, 1, 2, 2]
dc_horse = [-1, 1, -2, 2, -2, 2, -1, 1]

def bfs():
    queue = deque([(0, 0, 0, 0)])
    visited[0][0][0] = True

    while queue:
        r, c, k, dist = queue.popleft()

        if r == H-1 and c == W-1:
            return dist

        for d1 in range(4):
            nr = r + dr_monkey[d1]
            nc = c + dc_monkey[d1]

            if 0 <= nr < H and 0 <= nc < W:
                if not visited[k][nr][nc] and board[nr][nc] == 0:
                    visited[k][nr][nc] = True
                    queue.append((nr, nc, k, dist+1))

        if k < K:
            for d2 in range(8):
                nr = r + dr_horse[d2]
                nc = c + dc_horse[d2]

                if 0 <= nr < H and 0 <= nc < W:
                    if not visited[k+1][nr][nc] and board[nr][nc] == 0:
                        visited[k+1][nr][nc] = True
                        queue.append((nr, nc, k+1, dist+1))

    return -1


K = int(input())
W, H = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(H)]
visited = [[[False]*W for _ in range(H)] for _ in range(K+1)]
result = bfs()
print(result)
