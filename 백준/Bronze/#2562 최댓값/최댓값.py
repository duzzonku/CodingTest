#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2562                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2562                           #+#        #+#      #+#     #
#    Solved: 2026/02/04 16:48:07 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
max_val = 0
num_list = []

for i in range(9):
    num = int(input())
    num_list.append(num)
    if num_list[i] > max_val:
        max_val = num_list[i]
        max_index = i +1

print(max_val)
print(max_index)

