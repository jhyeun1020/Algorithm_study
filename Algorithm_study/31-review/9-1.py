cnt = int(input())
for a in map(int,input().split()):
    if a == 1:
        cnt -= 1
        continue
    for i in range(2, int(a ** 0.5) + 1):
        if a % i == 0:
            cnt -= 1
            break
print(cnt)