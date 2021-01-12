import math
for i in range(int(input())):
    a,b,c = map(int,input().split())
    room = 0
    # 층 설정
    if c%a == 0:
        room += a*100
    else:
        room += (c%a)*100
    # 방 번호 설정
    room += math.ceil(c/a)
    print(room)