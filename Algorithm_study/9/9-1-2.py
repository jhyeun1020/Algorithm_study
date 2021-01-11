# 시간 복잡도 좋음
slist = []
tlist = []
def d(n):
    count = 0
    for i in n:
        count += int(i)
    count += int(n)
    return count
for i in range(1,10001):
    k = d(str(i))
    slist.append(k)
    tlist.append(i)
a = set(slist)
b = set(tlist)
print(*sorted(b-a),sep = '\n')