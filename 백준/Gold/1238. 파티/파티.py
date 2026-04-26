import heapq
import sys

# 빠른 입력을 위해 추가
input = sys.stdin.readline
INF = float('inf')


def dijkstra(start, target_adj, N):
    dist = [INF] * (N + 1)
    dist[start] = 0
    # (현재 비용, 현재 노드)
    pq = [(0, start)]

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        # 이미 더 짧은 경로를 알고 있다면 스킵
        if dist[cur_node] < cur_cost:
            continue

        for next_cost, next_node in target_adj[cur_node]:
            cost = cur_cost + next_cost

            if cost < dist[next_node]:
                dist[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return dist

# 1. 입력 및 그래프 생성
N, M, X = map(int, input().split())

adj = [[] for _ in range(N + 1)]      # 정방향: X에서 집으로 (Return)
rev_adj = [[] for _ in range(N + 1)]  # 역방향: 집에서 X로 (Go)

for _ in range(M):
    A, B, T = map(int, input().split())
    adj[A].append((T, B))
    rev_adj[B].append((T, A))

# return_home[i]: X번 마을에서 i번 마을로 돌아가는 최단 시간
return_home = dijkstra(X, adj, N)
# go_to_party[i]: i번 마을에서 X번 마을로 가는 최단 시간
go_to_party = dijkstra(X, rev_adj, N)

# 3. 결과 합산 및 최댓값 찾기
max_time = 0
for i in range(1, N + 1):
    # 가는 시간 + 오는 시간
    total = return_home[i] + go_to_party[i]
    if total > max_time:
        max_time = total

print(max_time)