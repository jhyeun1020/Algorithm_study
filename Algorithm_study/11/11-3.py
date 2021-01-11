# 첫번째 케이스
number = [2,3,4,5,6,7,8,9,10,11]
eng = {'A':2,'B':2,'C':2,'D':3,'E':3,'F':3,'G':4,'H':4,'I':4,'J':5,'K':5,'L':5,'M': 6,'N':6,'O':6,'P':7,'Q':7,'R':7,'S':7,'T':8,'U':8,'V':8,'W':9,'X':9,'Y':9,'Z':9,}
cnt = 0
a = input()
for i in a:
    cnt += number[eng[i]-1]
print(cnt)

# 두번째 케이스
eng = ['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
a = input()
cnt = 0
for i in eng:
    for j in a:
        if j in i:
            cnt += eng.index(i)+3
print(cnt)