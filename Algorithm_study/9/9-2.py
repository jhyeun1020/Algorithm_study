# 첫번째 방법
def han(n):
    count = 0
    realcount = 0
    if int(n)<100:
        print(n)
    else:
        for j in range(100,int(n)+1):
            k = str(j)
            minus = int(k[1]) - int(k[0])
            for i in range(len(k) - 1):
                if int(k[i + 1]) - int(k[i]) == minus:
                    count += 1
            if count == len(k)-1:
                realcount += 1
            count = 0
        print(realcount + 99)
n = input()
han(n)