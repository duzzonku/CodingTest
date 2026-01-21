#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 30802                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/30802                          #+#        #+#      #+#     #
#    Solved: 2026/01/20 17:45:46 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #

n = int(input())
sizes = list(map(int, input().split()))
t, p = map(int, input().split())

total_shirt = 0
for s in sizes:
    if s%t==0:
        total_shirt+=(s//t)
    else:
        total_shirt+=(s//t)+1

pen_bun = n//p
pen_sin = n%p

print(total_shirt)
print(pen_bun, pen_sin)