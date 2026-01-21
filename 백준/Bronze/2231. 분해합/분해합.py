#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2231                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2231                           #+#        #+#      #+#     #
#    Solved: 2026/01/21 16:35:50 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
n = int(input())

result = 0

for i in range(1, n+1):
    decom_sum = i + sum(map(int, str(i)))

    if decom_sum == n:
        result = i
        break

print(result)