# 아스키 코드를 이용
a = input()
llist = []
for i in range(97,123):
    if chr(i) in a:
        llist.append(a.index(chr(i)))
    else:
        llist.append(-1)
print(*llist)

# 뭐가 있을까...
a = input()
for i in range(97,123):
    if chr(i) in a:
        print(a.index(chr(i)),end=' ')
    else:
        print('-1',end=' ')

# print(문자, end = '') -> end에 지정된 개행문자 \n을 ''로 바꿔줌
# print(문자, end = ' ') -> 개행문자 없이 1줄로 공백 한 칸을 추가하여 출력
# 문자열.find(요소) 함수 -> 지정한 요소를 찾으면 인덱스 번호 반환, 찾지 못한 경우 -1 반환
# 문자열.find() 함수와 리스트.index() 는 첫번째 인덱스 번호를 반호나
# find() 함수는 문자열에만 사용 가능