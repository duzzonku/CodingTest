N = int(input())
dist = list(map(int, input().split()))
expense = list(map(int, input().split()))

min_expense = expense[0]
result = 0

for i in range(len(expense) - 1):
    if expense[i] < min_expense:
        result += dist[i] * expense[i]
        min_expense = expense[i]
    else:
        result += dist[i] * min_expense

print(result)
