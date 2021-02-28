# 틀렸대요 혼자 다시 해결해보기
import math
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    dd = math.sqrt((x1 - x2)**2 + (y1 - y2)**2)
    if r1+r2 == dd:
        print(1)
    elif x1 == x2 and y1 == y2 and r1 == r2:
        print(-1)
    elif abs(r1-r2) > dd or r1+r2 < dd:
        print(0)
    else:
        print(2)