# 첫번째 방법
a,b = input().split()
c = ''; d=''
for i in a:
    c = i+c
for i in b:
    d = i+d
print(max(c,d))

# 두번째 방법
a,b = input().split()
a = list(a) ; b = list(b)
a.reverse() ; b.reverse()
a = ''.join(a) ; b = ''.join(b)
print(max(int(a),int(b)))

# k = k[::-1] 사용하면 k 리버스 됨