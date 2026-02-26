#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 1260                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/1260                           #+#        #+#      #+#     #
#    Solved: 2026/02/26 17:05:37 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque

def dfs(start_node):    
    if not visited1[start_node]:
        result1.append(start_node)
        visited1[start_node] = True

    for next_node in graph1[start_node]:
        if not visited1[next_node]:
            dfs(next_node)
    
    return result1




def bfs(start_node):
    queue = deque([start_node])
    visited2[start_node] = True

    while queue:
        cur = queue.popleft()
        result2.append(cur)
        
        for next_node in graph2[cur]:
            if not visited2[next_node]:
                queue.append(next_node)
                visited2[next_node] = True

    return result2



N, M, V = list(map(int, input().split()))

graph1 = [[] for _ in range(N+1)]
graph2 = [[] for _ in range(N+1)]

visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)

result1 = []
result2 = []

for _ in range(M):
    start, end = map(int, input().split())
    graph1[start].append(end)
    graph1[end].append(start)

    graph2[start].append(end)
    graph2[end].append(start)

for i in range(1, N + 1):
    graph1[i].sort()
    graph2[i].sort()


dfs_result = dfs(V)
bfs_result = bfs(V)

print(*dfs_result)
print(*bfs_result)