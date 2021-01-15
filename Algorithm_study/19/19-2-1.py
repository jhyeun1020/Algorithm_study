M, N = map(int,input().split())
che = []
for i in range(M,N+1):
    che.append(i)
ma = max(che)
j = 2
def prime():
    global j
    for i in range(M,N+1):
        if i%j ==0 and i != j and i in che:
            che.remove(i)
    j += 2 if j > 2 else 1
while j<ma**0.5:
    prime()
print(*che,sep='\n')