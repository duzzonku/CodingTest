from collections import deque
import heapq

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def island_labeling(N, board):
    island_num = 1
    visited = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            if board[i][j] == 1 and visited[i][j] == 0:
                bfs(i, j, island_num, visited)
                island_num += 1

    return island_num - 1, visited



def bfs(r, c, num, visited):
    queue = deque()
    queue.append((r, c))
    visited[r][c] = num

    while queue:
        cur_r, cur_c = queue.popleft()

        for d in range(4):
            nr = cur_r + dr[d]
            nc = cur_c + dc[d]

            if 0 <= nr < N and 0 <= nc < M:
                if board[nr][nc] == 1 and visited[nr][nc] == 0:
                    visited[nr][nc] = num
                    queue.append((nr, nc))



def make_bridges(island_count, visited):
    for r in range(N):
        for c in range(M):
            if visited[r][c] > 0:
                start_island = visited[r][c]

                for d in range(4):
                    dist = 0
                    nr = r + dr[d]
                    nc = c + dc[d]

                    while True:
                        if 0 <= nr < N and 0 <= nc < M:
                            end_island = visited[nr][nc]

                            if end_island == 0:
                                dist += 1
                                nr += dr[d]
                                nc += dc[d]

                            elif end_island == start_island:
                                break

                            else:
                                if dist >= 2:
                                    edges.append((dist, start_island, end_island))
                                break
                        else:
                            break


def prim(start_node, island_count):
    adj = [[] for _ in range(island_count + 1)]
    for dist, u, v in edges:
        adj[u].append((dist, v))
        adj[v].append((dist, u))

    distance = [float('inf')] * (island_count + 1)
    visited = [False] * (island_count + 1)

    pq = []
    heapq.heappush(pq, (0, start_node))

    total_weight = 0
    connected_island = 0

    while pq:
        cur_dist, cur_island = heapq.heappop(pq)

        if visited[cur_island]:
            continue

        visited[cur_island] = True
        total_weight += cur_dist
        connected_island += 1

        for next_dist, next_island in adj[cur_island]:
            if not visited[next_island] and next_dist < distance[next_island]:
                distance[next_island] = next_dist
                heapq.heappush(pq, (next_dist, next_island))

    if island_count == connected_island:
        return total_weight
    else:
        return -1
        



N, M = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(N)]

edges = []

island_count, visited_map = island_labeling(N, board)
make_bridges(island_count, visited_map)


if island_count > 0:
    ans = prim(1, island_count)
    print(ans)
else:
    print(0)
