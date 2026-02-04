n = int(input())

for i in range(n):
    ox_str = input()
    total_score = 0
    streak_score = 0

    for char in ox_str:
        if char == 'O':
            # O를 만나면 연속 점수 1 증가
            streak_score += 1
            # 늘어난 연속 점수를 총점에 더함
            total_score += streak_score
        else:
            # X를 만나면 연속 점수 리셋 (0점)
            streak_score = 0
            
    print(total_score)