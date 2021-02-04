# case 1 (정현아 이건 당최 무슨 코드냐 바보냐)
x, y, w, h = map(int,input().split())
if x<=w*0.5:
    if y >= h * 0.5:
        print(min(h - y, x))
    else:
        print(min(y,x))
else:
    if y >= h * 0.5:
        print(min(h - y, w-x))
    else:
        print(min(y, w-x))

# case 2
x, y, w, h = map(int,input().split())
print(min(x,y,w-x,h-y))