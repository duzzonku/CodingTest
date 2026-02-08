n = int(input())
ingredients = [list(map(int, input().split())) for _ in range(n)]

min_diff = 1000000000

for bit in range(1, 1 << n):
    sour = 1
    bitter = 0

    for i in range(n):
        if bit & (1 << i):
            sour *= ingredients[i][0]
            bitter += ingredients[i][1]

    diff = abs(sour - bitter)

    if diff < min_diff:
        min_diff = diff

print(min_diff)