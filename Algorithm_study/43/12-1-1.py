# case 3 (삽입 정렬 해보기)
N = int(input())
llist = [int(input()) for _ in range(N)]
for i in range(1,N):
    idx = i-1
    while idx >= 0 and llist[i] < llist[idx]:
        idx -= 1
    llist.insert(idx+1,llist[i])
    del llist[i+1]
print('\n'.join(map(str,llist)))