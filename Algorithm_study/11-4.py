# 첫번째
a = input()
cro = ['c=','c-','d-','lj','nj','s=','z=']
cnt = 0 ; cnt_dz = 0
for i in cro:
    if i in a :
        cnt += a.count(i)
if 'dz=' in a:
    cnt_dz += a.count('dz=')
    cnt -= cnt_dz
print(len(a)-(2*cnt)-(3*cnt_dz)+cnt+cnt_dz)