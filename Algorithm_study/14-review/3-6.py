# case 1
a = list(map(str,range(1,int(input())+1)))
a.reverse()
print(*a,sep='\n')
# case 2
a = int(input())
for i in range(a):
    print(a-i)