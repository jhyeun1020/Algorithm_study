a = int(input())
for _ in range(a):
    ratio = 0
    test = list(map(int,input().split()))
    mean = (sum(test)-test[0])/(len(test)-1)
    for i in range(len(test)):
        if i>0 and test[i]>mean:
            ratio += 1
    print("%0.3f%%"%((ratio/(len(test)-1))*100))