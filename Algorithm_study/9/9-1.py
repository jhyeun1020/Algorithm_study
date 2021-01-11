# 시간 복잡도 최악, 실행 후 5분 정도 지나고 나서야 출력 됨
a = []
b = []
def d(n):
    global a
    tmp = n
    number = 0
    for i in tmp:
        number += int(i)
    number += int(n)
    if number>=10000:
        return
    a.append(number)
    return d(str(number))
for i in range(1,10000):
    d(str(i))
s1 = list(set(a))
for i in range(1,10000):
    b.append(str(i))
for i in a:
    if str(i) in b:
        b.remove(str(i))
for i in range(len(b)):
    print(b[i])