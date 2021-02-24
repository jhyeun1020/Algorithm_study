import sys
N = int(sys.stdin.readline())
llist = [list(map(int,sys.stdin.readline().split())) for i in range(N)]
llist.sort()
for i in range(N):
    print(llist[i][0],llist[i][1])