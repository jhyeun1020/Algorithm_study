num = input()
cnt = 0
for i in num:
    if i == 'Z':
        cnt += 10
    elif i >= 'S':
        cnt += int((ord(i) - 66) / 3) + 3
    else:
        cnt += int((ord(i) - 65) / 3) + 3
print(cnt)