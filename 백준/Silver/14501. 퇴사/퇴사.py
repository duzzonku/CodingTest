def dfs(idx, cur_sum):
    global max_sum

    if idx >= N:
        max_sum = max(max_sum, cur_sum)
        return

    if idx + info[idx][0] <= N:
        dfs(idx + info[idx][0], cur_sum + info[idx][1]) 
    
    dfs(idx + 1, cur_sum)



N = int(input())
info = []
for tc in range(N):
    T, P = map(int, input().split())
    info.append((T, P))

    max_sum= 0   

dfs(0, 0)

print(max_sum)