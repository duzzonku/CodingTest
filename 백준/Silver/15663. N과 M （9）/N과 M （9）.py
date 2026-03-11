#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 15663                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/15663                          #+#        #+#      #+#     #
#    Solved: 2026/03/11 16:39:35 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
N, M = map(int, input().split())
num = list(map(int, input().split()))

visited = [False] * N
num.sort()
result = []

def backtracking(depth):
    if depth == M:
        print(*result)
        return
    
    prev_num = 0

    for i in range(N):
        if not visited[i]:
            if num[i] != prev_num:
                visited[i] = True
                prev_num = num[i]
                result.append(num[i])

                backtracking(depth + 1)

                visited[i] = False
                result.pop()

backtracking(0)