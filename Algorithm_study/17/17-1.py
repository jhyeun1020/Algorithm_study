def depth(k,n):
    global people
    if k == 1:
        people += sum(range(1,n+1))
        return
    for i in range(1, n+1):
        depth(k-1,i)
for _ in range(int(input())):
    k = int(input()) ; n = int(input())
    people = 0
    depth(k,n)
    print(people)