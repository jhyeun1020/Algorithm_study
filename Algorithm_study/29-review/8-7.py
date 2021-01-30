a = int(input())
cnt = 0
while a%5 != 0 and a>=3:
    a -= 3
    cnt += 1
if a%5 == 0:
    print(cnt+a//5)
else:
    print(-1)