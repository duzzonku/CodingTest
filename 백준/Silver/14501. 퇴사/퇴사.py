def dfs(day, cur_profit):
    global max_profit

    if day >= N:
        max_profit = max(max_profit, cur_profit)
        return

    if day + info[day][0] <= N:
        dfs(day + info[day][0], cur_profit + info[day][1])

    dfs(day + 1, cur_profit)


N = int(input())
info = []
for tc in range(1, N + 1):
    T, P = map(int, input().split())
    info.append((T, P))

max_profit = 0

dfs(0, 0)
print(max_profit)