# 카운팅 정렬을 흉내내 보았지만 메모리 초과로 실패
import sys

llist = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
clist = []
fin = [0 for _ in range(len(llist))]

for i in range(max(llist)):
    clist.append(llist.count(i+1))

# 누적합 계산
# clist의 인덱스 0은 1을 나타냄
for i in range(1, len(clist)):
    clist[i] += clist[i-1]

for i in range(len(llist)-1,-1,-1):
    clist[llist[i] - 1] -= 1
    fin[clist[llist[i]-1]] = llist[i]

sys.stdout.write('\n'.join(map(str,fin)))