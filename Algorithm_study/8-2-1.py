a = int(input())
for _ in range(a):
    ratio = 0
    len,*test = list(map(int,input().split()))
    mean = sum(test)/len
    for i in test:
        if i>mean:
            ratio += 1
    print("%0.3f%%"%(ratio/len*100))