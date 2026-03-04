from collections import deque

def bfs(start, end):
    queue = deque()
    queue.append((start, 0))
    visited[start] = True

    while queue:
        cur, time = queue.popleft()
        if cur == end:
            return time
        
        for dx in (cur-1, cur+1, 2*cur):
            nr = dx

            if 0 <= nr <= 100000:
                if not visited[nr]:
                    visited[nr] = True
                    queue.append((nr, time + 1))
    
    return time


N, K = map(int, input().split())
visited = [False] * 100001

result = bfs(N, K)
print(result)