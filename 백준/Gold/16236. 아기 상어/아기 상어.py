from collections import deque

dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def bfs(r, c, size):
    queue = deque()
    queue.append((r, c, 0))
    
    visited = [[False] * N for _ in range(N)]
    visited[r][c] = True
    fish_cnt = 0

    eat_fish = []

    while queue:
        cur_r, cur_c, dist = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if board[nr][nc] <= size:
                        visited[nr][nc] = True
                        queue.append((nr, nc, dist + 1))

                        if 0 < board[nr][nc] < size:
                            eat_fish.append((dist + 1, nr, nc))

    return eat_fish


N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

shark_r, shark_c = 0, 0
shark_size = 2
eat_count = 0
total_count = 0

for i in range(N):
    for j in range(N):
        if board[i][j] == 9:
            shark_r, shark_c = i, j
            board[shark_r][shark_c] = 0

while True:
    fishes = bfs(shark_r, shark_c, shark_size)

    if not fishes:
        break

    fishes.sort(key = lambda x : (x[0], x[1], x[2]))

    target_dist, target_r, target_c = fishes[0]

    total_count += target_dist
    shark_r, shark_c = target_r, target_c
    board[shark_r][shark_c] = 0
    eat_count += 1

    if eat_count == shark_size:
        shark_size += 1
        eat_count = 0

print(total_count)