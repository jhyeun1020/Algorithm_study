import sys
a = int(sys.stdin.readline())
cnt = 1 ; stack = 1

while cnt<a:
    stack += 1
    cnt += stack

if stack%2 == 0:
    print("{}/{}".format(a-cnt+stack, 1-a+cnt))
else:
    print("{}/{}".format(1-a+cnt,a-cnt+stack))