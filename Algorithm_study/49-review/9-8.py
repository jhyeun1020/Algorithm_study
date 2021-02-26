import sys
xlist = [] ; ylist = []
for i in range(3):
    a, b = map(int,sys.stdin.readline().split())
    xlist.append(a) ; ylist.append(b)
xlist.sort() ; ylist.sort()
print(xlist[2] if xlist[1] != xlist[2] else xlist[0], ylist[2] if ylist[1] != ylist[2] else ylist[0])