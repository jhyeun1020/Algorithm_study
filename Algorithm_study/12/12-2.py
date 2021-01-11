a = int(input())
cnt = 1
stack = 2
while ((a-1)/6)>cnt:
    cnt = cnt + stack
    stack += 1
if a == 1:
    print(1)
else:
    print(stack)