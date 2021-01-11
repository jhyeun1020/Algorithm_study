c = [] ; cnt = 0 ; find = [] ; cons = ''
for _ in range(int(input())):
    a = list(input())
    if len(a) == len(set(a)):
        cnt += 1
    else:
        cnt1 = 1
        find.clear()
        for i in a:
            if i not in find:
                find.append(i)
                cons = i
            else:
                if i != cons:
                    cnt1 = 0
        if cnt1:
            cnt += 1
print(cnt)