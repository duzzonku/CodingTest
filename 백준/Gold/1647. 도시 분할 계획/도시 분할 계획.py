import heapq
import sys

input = sys.stdin.readline

def prim():
    visited = [False] * (N + 1)
    # 현재 비용, 시작 노드
    pq = [(0, 1)]

    total_cost = 0
    max_edge = 0
    count = 0

    while pq:
        cur_cost, cur_node = heapq.heappop(pq)

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        total_cost += cur_cost
        max_edge = max(max_edge, cur_cost)
        count += 1

        if count == N:
            break

        for next_cost, next_node in adj[cur_node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_cost, next_node))

    print(total_cost - max_edge)



N, M = map(int, input().split())
adj =[[] for _ in range(N + 1)]
for _ in range(M):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))

prim()
