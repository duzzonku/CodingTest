#  **************************************************************************  #
#                                                                              #
#                                                       :::    :::    :::      #
#    Problem Number: 2580                              :+:    :+:      :+:     #
#                                                     +:+    +:+        +:+    #
#    By: songkh724 <boj.kr/u/songkh724>              +#+    +#+          +#+   #
#                                                   +#+      +#+        +#+    #
#    https://boj.kr/2580                           #+#        #+#      #+#     #
#    Solved: 2026/02/27 17:26:58 by songkh724     ###          ###   ##.kr     #
#                                                                              #
#  **************************************************************************  #
def check(r, c, n):
    for i in range(9):
        if board[r][i] == n:
            return False
    
    for j in range(9):
        if board[j][c] == n:
            return False
        
    start_r =  (r//3) * 3
    start_c =  (c//3) * 3
    
    for i in range(3):
        for j in range(3):
            if board[start_r + i][start_c + j] == n:
                return False
            
    return True
    

def solve(idx):
    if idx == len(blank):
        for x in board:
            print(*x)
        exit()
        return
    
    cur_r, cur_c = blank[idx]

    for i in range(1, 10):
        if check(cur_r, cur_c, i):
            board[cur_r][cur_c] = i
            solve(idx + 1)
            board[cur_r][cur_c] = 0



board = [list(map(int, input().split())) for _ in range(9)]

blank = []

for row in range(9):
    for col in range(9):
        if board[row][col] == 0:
            blank.append((row, col))

solve(0)
