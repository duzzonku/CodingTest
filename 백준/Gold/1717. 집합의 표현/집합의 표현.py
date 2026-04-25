def find_set(x):
    if parent[x] != x:
        parent[x] = find_set(parent[x])
    return parent[x]

def union(a, b):
    root_a = find_set(a)
    root_b = find_set(b)

    if root_a != root_b:
        if root_a < root_b:
            parent[root_a] = root_b
        else:
            parent[root_b] = root_a


n, m = map(int, input().split())

parent = [i for i in range(n + 1)]

for _ in range(m):
    r, a, b = map(int, input().split())

    if r == 0:
        union(a, b)

    if r == 1:
        if find_set(a) != find_set(b):
            print('NO')
        else:
            print("YES")