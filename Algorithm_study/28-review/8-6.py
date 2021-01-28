for _ in range(int(input())):
    a = int(input()) ; b = int(input())
    llist = []
    for i in range(b):
        llist.append(i + 1)
    for i in range(a):
        for j in range(1,b):
            llist[j] = llist[j] + llist[j-1]
    print(llist[-1])