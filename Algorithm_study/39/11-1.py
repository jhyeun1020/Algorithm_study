N, M = map(int,input().split())
c = list(map(int,input().split()))
llist = []
for i in c:
    for j in c:
        for k in c:
            if i == j or j == k or k == i:
                continue
            if i+j+k<=M:
                llist.append(i+j+k)
print(max(llist))
# 이거 무조건 시간 초과 각인데 왜 된건지 모르겠네요
# 다시 해봅시다!