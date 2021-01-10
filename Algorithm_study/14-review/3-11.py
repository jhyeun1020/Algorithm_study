a, b = map(int,input().split())
c = list(map(int,input().split()))
print(*[i for i in c if i<b])