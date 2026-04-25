from collections import deque

def dfs(start_node):
    visited[start_node] = True
    print(start_node, end=' ')

    for next_node in adj[start_node]:
        if not visited[next_node]:
            visited[next_node] = True
            dfs(next_node)
    return


def bfs(start_node):
    queue = deque()
    queue.append(start_node)
    visited[start_node] = True

    while queue:
        cur_node = queue.popleft()
        print(cur_node, end=' ')

        for next_node in adj[cur_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)
    return



N, M, V = map(int, input().split())
adj = [[] for _ in range(N + 1)]

for _ in range(M):
    A, B = map(int, input().split())
    adj[A].append(B)
    adj[B].append(A)

for i in range(N + 1):
    adj[i].sort()

visited = [False] * (N + 1)
dfs(V)

print()

visited = [False] * (N + 1)
bfs(V)