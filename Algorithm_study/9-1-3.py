# 소거하는 방법이 아닌 셀프 넘버를 찾는 알고리즘을 짜보자
# 백준에다가 제출하면 시간 초과 오류가 남
a = []
def d():
    for i in range(2, 10001):
        for j in range(1, i):
            k = j + j // 1000 + (j // 100) % 10 + (j // 10) % 10 + j % 10
            a.append(k)
        if i in a:
            pass
        else:
            print(i)
        a.clear()
print(1)
d()