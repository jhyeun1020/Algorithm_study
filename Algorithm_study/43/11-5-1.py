# case 2
N = int(input())
stack = 0
num = 666
while 1:
    if '666' in str(num):
        stack += 1
    if stack == N:
        print(num)
        break
    num += 1