import sys
N = int(sys.stdin.readline())
llist = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
llist.sort(key = lambda x:(x[1],x[0]))
for i in range(N):
    print(llist[i][0],llist[i][1])