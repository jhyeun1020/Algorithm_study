alphabet = 'abcdefghijklmnopqrstuvwxyz'
a = input()
for i in alphabet:
    if i in a:
        print(a.index(i),end=' ')
    else:
        print(-1,end=' ')
# find 함수는 없을 시 -1을 반환