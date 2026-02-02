n, k = map(int, input().split())

people = list(range(1, n + 1))
result = []

idx = 0

while people:
    idx = (idx + (k - 1)) % len(people)
    pop_num = people.pop(idx)
    result.append(pop_num)

print('<' + ', '.join(map(str, result)) + '>')