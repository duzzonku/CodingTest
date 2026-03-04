def dfs(player_idx, cur_sum):
    global max_sum

    if player_idx == 11:
        if cur_sum > max_sum:
            max_sum = cur_sum
        return

    for i in range(11):
        if not visited[i]:
            if pos[player_idx][i] != 0:
                visited[i] = True
                dfs(player_idx+1, cur_sum + pos[player_idx][i])
                visited[i] = False

C = int(input())
for _ in range(C):
    pos = [list(map(int, input().split())) for _ in range(11)]
    visited = [False] * 11
    max_sum = 0

    dfs(0, 0)
    print(max_sum)            
