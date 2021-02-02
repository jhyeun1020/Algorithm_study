def sosu(a):
    cnt = 2 * a - a
    for i in range(a + 1, 2 * a + 1):
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                cnt -=1
                break
    print(cnt)
while 1:
    a = int(input())
    if a == 0:
        break
    sosu(a)