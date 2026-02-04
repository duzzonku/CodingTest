#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 10818                             :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/10818                          #+#        #+#      #+#     #
#    Solved: 2026/02/04 16:58:10 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())
num = list(map(int, input().split()))

max_val = num[0]
min_val = num[0]


for i in num:

    if i > max_val:
        max_val = i
    
    if i < min_val:
        min_val = i
    
print(min_val, max_val)
