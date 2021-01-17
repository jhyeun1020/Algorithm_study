for _ in range(int(input())):
    a,*b = [i for i in map(int,input().split())]
    c = [j for j in b if j>sum(b)/a]
    print("%0.3f%%"%(len(c)/a*100))