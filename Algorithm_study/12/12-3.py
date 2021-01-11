import sys
a = int(sys.stdin.readline())
cnt = 1 ; stack = 1

for i in range(1,a+1):
    if i > cnt:
        stack += 1
        cnt += stack

if stack % 2 == 0:
    print("{}/{}".format(a - cnt+stack,1 - a + cnt))
else:
    print("{}/{}".format(cnt + 1- a,a - cnt+stack))