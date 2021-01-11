cnt = 0 ; c=100
b = int(input())
a = b
while a != c:
    c = b
    a = (a%10)*10 + (a//10+a%10)%10
    cnt += 1
print(cnt)