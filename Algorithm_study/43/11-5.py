# case 1
llist = []
stack = 666
while len(llist) <= 10000:
    if '666' in str(stack):
        llist.append(stack)
    stack += 1
print(llist[int(input())-1])