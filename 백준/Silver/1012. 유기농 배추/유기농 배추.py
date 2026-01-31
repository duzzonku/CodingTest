import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def dfs(x, y):
    graph[y][x] = 0
    
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if (0 <= nx < m) and (0 <= ny < n) and graph[ny][nx] == 1:
            dfs(nx, ny)

t = int(input()) 

for _ in range(t):
    m, n, k = map(int, input().split())
    graph = [[0]*m for _ in range(n)]

    for _ in range(k):
        x, y = map(int, input().split())
        graph[y][x] = 1

    count = 0
    for i in range(n):    
        for j in range(m): 
            if graph[i][j] == 1:
                dfs(j, i)  
                count += 1 

    print(count)