#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2644                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2644                           #+#        #+#      #+#     #
#    Solved: 2026/02/26 14:58:03 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
from collections import deque
import sys

input = sys.stdin.readline

def bfs(start_node):
    queue = deque([start_node])
    visited[start_node] = 0

    while queue:
        cur = queue.popleft()

        if cur == end:
            return visited[cur]
        
        for next_node in graph[cur]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur]+1
        
                queue.append(next_node)
    
    return -1




n = int(input())
start, end = map(int, input().split())
m = int(input())
graph = [[] for _ in range(n+1)]
visited = [-1]*(n+1)

for _ in range(m):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

result = bfs(start)
print(result)