import sys
import heapq

n = int(sys.stdin.readline())
arr = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x > 0:
        heapq.heappush(arr, x)

    elif x == 0:
        if not arr:
            print(0)
        else:
            print(heapq.heappop(arr))
