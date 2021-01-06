# 문자열을 입력받고 문자의 아스키 코드 값과 그 문자의 인덱스의 곱 top3의 합을 출력하시오
a = input()
b = []
for i in range(len(a)):
    b.append(ord(a[i])*i)
print(b)
b.sort()
b.reverse()
print(b[0]+b[1]+b[2])