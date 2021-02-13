# case 1
slist = []
N = int(input())
for _ in range(N):
    slist.append(int(input()))
slist.sort()
for i in range(N):
    print(slist[i])

# case 2 (버블 정렬)
slist = []
N = int(input())
for _ in range(N):
    slist.append(int(input()))
for j in range(N-1):
    for i in range(1, N-j):
        if slist[i] < slist[i - 1]:
            slist[i], slist[i - 1] = slist[i - 1], slist[i]
for i in range(N):
    print(slist[i])