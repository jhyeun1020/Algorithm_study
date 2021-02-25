llist = [input() for _ in range(int(input()))]
llist = set(llist)
llist = sorted(llist, key = lambda x:(len(x),x))
for i in range(len(llist)):
    print(llist[i])