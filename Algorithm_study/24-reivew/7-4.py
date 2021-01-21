for _ in range(int(input())):
    a, b = input().split()
    a = [i*int(a) for i in b]
    print(*a,sep='')