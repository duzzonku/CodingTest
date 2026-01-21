import sys
N = int(sys.stdin.readline())

member_list = []

for i in range(1,N+1):
    age, name = sys.stdin.readline().split()
    member_list.append([int(age), name])

member_list.sort(key = lambda x: x[0])

for m in member_list:
    print(*m)