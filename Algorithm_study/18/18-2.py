# 틀린 문제
# 다시 복습하도록 !!
for _ in range(int(input())):
    x, y = map(int,input().split())
    lenth = y-x #시작과 끝을 빼고 이동해야 할 거리
    cnt = 0
    can = [-1,0,1]
    while lenth > 0:
        for i in can:
            if i == lenth and i == 1:
                cnt += 1
                break
        if lenth > sum(range(1,can[2]+1)):
            cnt += 1
            lenth -= can[2]
            can = [can[2]-1,can[2],can[2]+1]
        elif lenth == sum(range(1,can[2]+1)):
            cnt += 1
            lenth -= can[1]
        elif lenth < sum(range(1,can[2]+1)):
            cnt += 1
            lenth -= can[0]
            can = [can[0]-1,can[0],can[0]+1]
    print(cnt)