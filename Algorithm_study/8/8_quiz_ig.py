# 드레이븐의 Q 스킬은 스택을 쌓습니다.
# 스택은 무조건 정수로 취급합니다.
# 일반 미니언은 스택 1개
# 대포 미니언은 스택 2개
# 챔피언을 죽일 시 스택이 2배가 됩니다.
# 챔피언에게 죽을 시 스택의 75%를 잃습니다.
# 일반 미니언 A, 대포 미니언 B, 챔피언을 죽일 시 O, 챔피언에게 죽을 시 X 일때
# 단 미니언으로 스택을 연속으로 쌓을시 다음 스택 1개가 추가됩니다.(무한 중첩 가능)
# 입력을 받고 최종적으로 남아있는 스택을 출력하시오
# 입력 데이터셋:
# AABAABAAAAOAABXXBOO
data = input()
stack = 0
min_stack = 0
for i in data:
    if i == 'A':
        stack += 1
        stack += min_stack
        min_stack += 1
    elif i == 'B':
        stack += 2
        stack += min_stack
        min_stack += 1
    if i == 'O':
        stack = stack*2
        min_stack = 0
    elif i == 'X':
        stack = round(stack*0.25)
        min_stack = 0
print(stack)