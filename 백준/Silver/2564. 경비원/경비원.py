W, H = map(int, input().split())
N = int(input())

stores = []
for _ in range(N):
    stores.append(list(map(int, input().split())))

guard_direction, guard_dist = map(int, input().split())

def get_distance(direction, dist):
    if direction == 1: #북
        return dist
    elif direction == 4: #동
        return W + dist
    elif direction == 2: #남
        return W + H + (W-dist)
    elif direction == 3: #서
        return W + H + W + (H-dist)
    
total_perimeter = 2 * (W+H) #전체 둘레
guard_pos = get_distance(guard_direction, guard_dist)
ans = 0

for s_dir, s_dist in stores:
    stores_pos = get_distance(s_dir, s_dist)

    path1 = abs(guard_pos - stores_pos)
    path2 = total_perimeter - path1

    ans += min(path1, path2)

print(ans)