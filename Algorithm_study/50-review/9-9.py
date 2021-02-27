while 1:
    llist = list(map(int,input().split()))
    if 0 in llist:
        break
    llist.sort()
    if llist[2]**2 == llist[0]**2 + llist[1]**2:
        print('right')
    else:
        print('wrong')