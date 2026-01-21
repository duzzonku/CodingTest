import sys

N = int(sys.stdin.readline())

coordinate = []

for i in range(1,N+1):
    x, y = map(int, sys.stdin.readline().split())
    coordinate.append([x, y])

coordinate.sort(key=lambda x: (x[0], x[1]))

for result in coordinate:
    print(*result)