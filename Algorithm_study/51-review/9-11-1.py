for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    '''r1과 r2가 같고 거리가 0인 경우 두번째 조건의 경우도 만족하므로 
    두 원이 일치할 때의 조건을 가장 먼저 설정해야 함'''
    if dis == 0 and r1 == r2:
        print(-1)
    elif dis == r1+r2 or dis == abs(r1-r2):
        print(1)
    elif r1+r2-dis > 0 and abs(r1-r2) < dis:
        print(2)
    else:
        print(0)