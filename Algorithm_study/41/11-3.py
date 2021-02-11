wlist = []
hlist = []
for _ in range(int(input())):
    a, b = map(int,input().split())
    wlist.append(a) ; hlist.append(b)
for i in range(len(wlist)):
    stack = 0
    for j in range(len(wlist)):
        if wlist[i] < wlist[j] and hlist[i] < hlist[j]:
            stack += 1
    print(stack+1,end=' ')