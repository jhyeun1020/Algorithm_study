import sys
for i in range(int(sys.stdin.readline())):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #{}: {}".format(i+1,a+b))