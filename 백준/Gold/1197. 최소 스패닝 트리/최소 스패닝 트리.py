import heapq

def prim(start_node):
    pq = []
    heapq.heappush(pq, (0, start_node))

    total_weight = 0
    node_count = 0

    while pq:
        weight, cur_node = heapq.heappop(pq)

        if visited[cur_node]:
            continue

        visited[cur_node] = True
        node_count += 1
        total_weight += weight

        for next_weight, next_node in adj[cur_node]:
            if not visited[next_node]:
                heapq.heappush(pq, (next_weight, next_node))

    return total_weight


V, E = map(int, input().split())

visited = [False] * (V + 1) 
adj  = [[] for _ in range(V + 1)]

for _ in range(E):
    A, B, C = map(int, input().split())
    adj[A].append((C, B))
    adj[B].append((C, A))

ans = prim(1)
print(ans)