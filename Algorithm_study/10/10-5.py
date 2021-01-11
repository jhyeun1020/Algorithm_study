a = (input()).upper()
b = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
c = {}
for i in b:
    if i in a:
        c[i] = a.count(i)
cnt = 0
for i in c.values():
    if i == max(c.values()):
        cnt += 1
if cnt > 1:
    print('?')
else:
    for i in c:
        if c[i] == max(c.values()):
            print(i)