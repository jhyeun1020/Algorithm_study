input()
a = list(map(int, input().split()))
cnt = 0
for i in a:
    right = 0
    for j in range(1,i+1):
        if i % j == 0:
            if j == i or j == 1:
                pass
            else:
                right += 1
    if right == 0:
        cnt += 1
if 1 in a:
    print(cnt-1)
else:
    print(cnt)