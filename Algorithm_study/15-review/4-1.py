# case 1
while 1:
    a,b = (map(int,input().split()))
    if a == 0 and b == 0:
        break
    else:
        print(a+b)
# case 2
a,b = map(int,input().split)
while a != 0 and b != 0:
    print(a+b)
    a, b = map(int, input().split)