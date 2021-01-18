# 백준 통못
while 1:
    n = int(input())
    if n == 0:
        break
    else:
        count = 0
        for i in range(n+1,2*n+1):
            cnt = 0
            if i == 2:
                count += 1
            else:
                for j in range(2,i):
                    if i % j == 0:
                        cnt += 1
                if cnt == 0:
                    count +=1
        print(count)