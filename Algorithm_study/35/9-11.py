import math
for _ in range(int(input())):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    d = math.sqrt(abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2)
    a = [d,r1,r2]
    m = max(a)
    a.remove(max(a))
    if d == 0 and r1 == r2:
        print(-1)
    elif d == (r1+r2) or max(r1,r2) == d+min(r1,r2):
        print(1)
    elif m > sum(a):
        print(0)
    else:
        print(2)