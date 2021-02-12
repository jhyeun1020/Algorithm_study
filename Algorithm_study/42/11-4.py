N, M = map(int,input().split())
llist = [input() for _ in range(M)]
stack1 = 0
line = 0
for i in range(N):
    line += 1
    order = 0
    for j in range(M):
        order += 1
        if line % 2 == 0:
            if order % 2 == 0:
                if llist[i][j] != 'W':
                    stack1 += 1
            else:
                if llist[i][j] != 'B':
                    stack1 += 1
        else:
            if order % 2 == 0:
                if llist[i][j] != 'B':
                    stack1 += 1
            else:
                if llist[i][j] != 'W':
                    stack1 += 1