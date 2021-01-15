N = int(input())
div = []
while N != 1:
    for i in range(2, N + 1):
        if N % i == 0:
            div.append(i)
            N = int(N / i)
            break
print(*div,sep = '\n')