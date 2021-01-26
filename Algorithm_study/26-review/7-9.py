# case 1
cro = ['c=','c-','dz=','d-','lj','nj','s=','z=']
a = input()
count = 0
rcount = 0
for i in cro:
    if i in a:
        count += a.count(i)
        if i == 'dz=':
            count -= 1
            rcount += 1
print(len(a)-(rcount*3)-(count-rcount)*2+count)

# case 2
a = input()
print(len(a)-sum(a.count(i) for i in ['=','-','lj','nj','dz=']))