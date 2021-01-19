num = []
for i in range(1,10001):
    num.append(i)
def han(i):
    i = str(i)
    next = 0
    for j in range(len(i)):
        next += int(i[j])
    next += int(i)
    if next in num:
        num.remove(next)
for i in range(1,10001):
    han(i)
print(*num,sep='\n')