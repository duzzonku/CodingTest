N = int(input())
numbers = list(map(int, input().split()))
add, sub, mul, div = map(int, input().split())

max_val = -int(1e9)
min_val = int(1e9)


def dfs(idx, current_val, plus, minus, multiply, divide):
    global max_val, min_val

    if idx == N:
        max_val = max(max_val, current_val)
        min_val = min(min_val, current_val)
        return

    if plus > 0:
        dfs(idx + 1, current_val + numbers[idx], plus - 1, minus, multiply, divide )

    if minus > 0:
        dfs(idx + 1, current_val - numbers[idx], plus, minus - 1, multiply, divide)

    if multiply > 0:
        dfs(idx + 1, current_val * numbers[idx], plus, minus, multiply - 1, divide)

    if divide > 0:
        dfs(idx + 1, int(current_val / numbers[idx]), plus, minus, multiply, divide - 1)

    return
    
dfs(1, numbers[0], add, sub, mul, div)

print(max_val)
print(min_val)