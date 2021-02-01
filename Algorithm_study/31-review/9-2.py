a = int(input()) ; b = int(input())
llist = [i for i in range(a,b+1)]
for j in range(a,b+1):
    if j == 1:
        llist.remove(j)
        continue
    for i in range(2, int(j ** 0.5) + 1):
        if j % i == 0:
            llist.remove(j)
            break
if len(llist) == 0:
    print(-1)
else:
    print(sum(llist),min(llist),sep='\n')