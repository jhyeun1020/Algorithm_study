x = [] ; y = []
for i in range(3):
    a, b = map(int,input().split())
    x.append(a) ; y.append(b)
x = sorted(x,key=x.count) ; y = sorted(y,key=y.count)
print(x[0],y[0])