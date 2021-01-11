# 리스트 안쓰고
cnt = 0
for i in input():
    if i == 'Z':
        cnt += 10
    elif ord(i) >= ord('S') :
        cnt += (ord(i) - 63) // 3 + 2
    else:
        cnt += (ord(i) - 62) // 3 + 2
print(cnt)