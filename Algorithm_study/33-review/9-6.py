prime = 10000*[True]
for i in range(2,int(10000**0.5)+1):
    if prime[i-1]:
        for j in range(2*i,10001,i):
            prime[j-1] = False
for _ in range(int(input())):
    a = int(input())
    llist = [1,2]
    for i in range(2,int(a*0.5)+1):
        if prime[i-1] and prime[a-i-1]:
            llist[0] = i ; llist[1] = a-i
    print(llist[0],llist[1])