llist = []
for _ in range(int(input())):
    llist.append(int(input()))
len2 = len(llist)
llist.sort()

print(round(sum(llist) / len2))

print(llist[len2 // 2])

clist = {}
for i in range(len2):
    count2 = llist.count(llist[i])
    clist[llist[i]] = count2
rmax = clist[max(clist)]
flist = {}
for k, v in clist.items():
    if v == rmax:
        flist[k] = v
if len(flist) > 1:
    i = 0
    for k, v in flist.items():
        if i == 1:
            print(k)
            break
        i += 1
else:
    print(max(flist))

print(max(llist)-min(llist))
# 틀림 Counter 함수를 사용하여 복습 때 다시 하기