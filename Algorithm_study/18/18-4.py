a = []
for i in range(int(input()),int(input())+1):
    cnt = 0
    if i == 1:
        cnt += 1
    else:
        for j in range(2, i):
            if i % j == 0:
                cnt += 1
    if cnt == 0:
        a.append(i)
if len(a) == 0:
    print(-1)
else:
    print(sum(a))
    print(min(a))