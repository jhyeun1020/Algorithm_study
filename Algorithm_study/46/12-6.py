import sys
n = int(sys.stdin.readline())
xlist = [] ; ylist=[]
for _ in range(n):
    a, b = map(int,sys.stdin.readline().split())
    xlist.append(a)
    ylist.append(b)
for i in range(n):
    for j in range(n-(i+1)):
        if xlist[j] > xlist[j+1]:
            xlist[j], xlist[j+1] = xlist[j+1], xlist[j]
            ylist[j], ylist[j + 1] = ylist[j + 1], ylist[j]
        elif xlist[j] == xlist[j+1]:
            if ylist[j] > ylist[j+1]:
                xlist[j], xlist[j + 1] = xlist[j + 1], xlist[j]
                ylist[j], ylist[j + 1] = ylist[j + 1], ylist[j]
for i in range(n):
    print(xlist[i], ylist[i])