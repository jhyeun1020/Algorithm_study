cnt = 0
for i in range(1,int(input())+1):
    i = str(i)
    if len(i) <= 2:
        cnt += 1
    elif len(i) == 3:
        if (int(i[0])+int(i[2]))/2 == int(i[1]):
            cnt += 1
print(cnt)