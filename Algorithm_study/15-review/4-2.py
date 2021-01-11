# case 1 -> 입력이 없을 때 빈 문자열을 반환 -> EOFerror로부터 안전
import sys
while 1:
    try:
        a, b = map(int, sys.stdin.readline().split())
        print(a+b)
    except ValueError:
        break
# case 2 -> 입력이 없을 때 EOFerror를 반환
while 1:
    try:
        a, b = map(int, input().split())
        print(a + b)
    except:
        break