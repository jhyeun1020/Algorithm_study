while 1:
    side = list(map(int,input().split()))
    if side[0] == 0 and side[1] == 0 and side[2] == 0:
        break
    side.sort()
    if side[0]**2+side[1]**2 == side[2]**2:
        print("right")
    else:
        print("wrong")