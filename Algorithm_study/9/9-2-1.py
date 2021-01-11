# 두번째 방법
# 입력 값이 3자리 수까지일 때를 가정
def han(n):
    cnt = 0
    if int(n)<100:
        print(n)
    else:
        for i in range(100,int(n)+1):
            j = str(i)
            if (int(j[0])+int(j[2]))/2 == int(j[1]):
                cnt += 1
        print(99+cnt)
han(input())