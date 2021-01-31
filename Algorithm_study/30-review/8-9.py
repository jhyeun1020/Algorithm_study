for _ in range(int(input())):
    x, y = map(int,input().split())
    range = y-x
    if range < 3:
        print(range)
    else:
        a = 3
        stack = 3
        kk = 2
        while 1:
            if a <= range < a+kk:
                print(stack)
                break
            a += kk
            stack += 1
            if stack % 2 != 0:
                kk += 1