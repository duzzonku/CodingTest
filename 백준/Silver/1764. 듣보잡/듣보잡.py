import sys

n, m = map(int, sys.stdin.readline().split())

no_listen_people = set()
for group1 in range(n):
    no_listen_people.add(sys.stdin.readline().strip())

no_see_people = set()
for group2 in range(m):
    no_see_people.add(sys.stdin.readline().strip())

group = no_listen_people.intersection(no_see_people)
group = sorted(group)

print(len(group))

for result in group:
    print(result)