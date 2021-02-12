N, M = map(int,input().split())
llist = [input() for _ in range(N)]
clist = []
for i in range(N-7):
    for j in range(M-7):
        W = 0
        B = 0
        for a in range(i,i+8):
            for b in range(j,j+8):
                if (a+b)%2 == 0:
                    if llist[a][b] != 'W':
                        W += 1
                    if llist[a][b] != 'B':
                        B += 1
                else:
                    if llist[a][b] != 'B':
                        W += 1
                    if llist[a][b] != 'W':
                        B += 1
        clist.append(W)
        clist.append(B)
print(min(clist))