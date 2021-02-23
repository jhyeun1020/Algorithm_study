# case 1
a = input()
llist = []
for i in a:
    llist.append(i)
llist = list(map(int,llist))
llist.sort(reverse=True)
print(*llist,sep='')
# case 2
print(''.join(sorted(input())[::-1]))