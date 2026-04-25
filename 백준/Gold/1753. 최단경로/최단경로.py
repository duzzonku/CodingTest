import heapq
import sys

input = sys.stdin.readline


def dijkstra(start):
    distance = [float('inf')] * (V + 1)

    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        cur_weight, cur_node = heapq.heappop(pq)

        if cur_weight > distance[cur_node]:
            continue

        for next_weight, next_node in adj[cur_node]:
            cost = cur_weight + next_weight

            if cost < distance[next_node]:
                distance[next_node] = cost
                heapq.heappush(pq, (cost, next_node))

    return distance



V, E = map(int, input().split())
K = int(input())

adj = [[] for _ in range(V + 1)]

for _ in range(E):
    u, v, w = map(int, input().split())
    adj[u].append((w, v))

ans = dijkstra(K)

for i in range(1, V + 1):
    if ans[i] == float('inf'):
        print('INF')
    else:
        print(ans[i])