#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2609                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2609                           #+#        #+#      #+#     #
#    Solved: 2026/01/21 17:43:29 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
num1, num2 = map(int, input().split())

result1 = []
for i in range(1, num1+1):
    if (num1%i==0) & (num2%i==0):
        result1=i


result2 = []
for i in range(1, num2+1):
    result2 = int(result1 * (num1/result1) * (num2/result1))

print(result1)
print(result2)