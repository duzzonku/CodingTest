import sys
input = sys.stdin.readline

n, m = map(int, input().split())

pok_name_dict = {}
pok_id_dict = {}

for i in range(1, n+1):
    name = input().strip()
    pok_name_dict[name] = i
    pok_id_dict[i] = name

for j in range(m):
    mission = input().strip()

    if mission.isalpha():
        print(pok_name_dict[mission])
    else:
        print(pok_id_dict[int(mission)])