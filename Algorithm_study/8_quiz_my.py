# 내가 만든 문제
# 농구 선수 다섯명이 골을 넣었을 때 골을 연속해서 넣으면 연속한 개수만큼 점수의 가치가 1점씩 늘어난다
# ex) 연속해서 2 골일 시 연속한 골의 점수는 2점, 연속해서 5 골일 시 연속한 골의 점수는 5점
# 이때 모든 선수들의 평균 점수를 소수점 둘째자리까지 구하고
# 평균을 넘는 선수들의 비율을 소수점 셋제자리까지 구해보자
# 입력 데이터 셋:
"""5
OOXXXXOOXOXOX
OOOOOXXXOXXXO
OOXXOXOOOXXX
OOOXXXXXXXOXOX
XXXXXXOOOXOXOX"""
first = int(input())
stack = 0 ; player_score = []
for i in range(first):
    player = input()
    score = 0
    for j in range(len(player)):
        if player[j] == 'O':
            stack += 1
        else:
            stack = 0
        if (j<(len(player)-1) and player[j+1] != 'O') or j == len(player)-1:
            score += stack **2
            stack = 0
    player_score.append(score)
mean = sum(player_score) / first
print("평균 점수: %.2f" % mean)
print("평균을 넘는 선수 비율: %.3f%%"%(len([x for x in player_score if x > mean])/first*100))