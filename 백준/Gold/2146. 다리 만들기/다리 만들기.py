dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


# 섬 번호 붙이기
def bfs(r, c, island_id):
    queue = []
    queue.append((r, c))
    island_map[r][c] = island_id

    while queue:
        cur_r, cur_c = queue.pop(0)

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if island_map[nr][nc] == 0 and board[nr][nc] == 1:
                    island_map[nr][nc] = island_id
                    queue.append((nr, nc))

    island_id += 1


# 최단 거리 찾기
def find_dist(cur_island):
    global min_dist

    distance = [[float('inf')] * N for _ in range(N)]
    queue = []

    for r in range(N):
        for c in range(N):
            if island_map[r][c] == cur_island:
                queue.append((r, c))
                distance[r][c] = 0

    while queue:
        cur_r, cur_c = queue.pop(0)

        if distance[cur_r][cur_c] >= min_dist:
            return

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < N:
                if island_map[nr][nc] > 0 and island_map[nr][nc] != cur_island:
                    min_dist = min(min_dist, distance[cur_r][cur_c])
                    return

                if island_map[nr][nc] == 0 and distance[nr][nc] == float('inf'):
                    distance[nr][nc] = distance[cur_r][cur_c] + 1
                    queue.append((nr, nc))



N = int(input())
board = [list(map(int, input().split())) for _ in range(N)]

island_map = [[0] * N for _ in range(N)]
island_id = 1


min_dist = 9999

for r in range(N):
    for c in range(N):
        if board[r][c] == 1 and island_map[r][c] == 0:
            bfs(r, c, island_id)
            island_id += 1

for i in range(1, island_id):
    find_dist(i)

print(min_dist)