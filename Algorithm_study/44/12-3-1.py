import sys
N = int(sys.stdin.readline())
llist = [0]*10000
for i in range(N):
    llist[int(sys.stdin.readline())-1] += 1
for i in range(10000):
    if llist[i] != 0:
        for j in range(llist[i]):
            sys.stdout.write(str(i+1)+'\n')