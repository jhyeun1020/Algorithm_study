# 백준 통못
import sys
def sosu(n):
    if n == 1:
        return False
    for j in range(2, int(n ** 0.5)+1):
        if n % j == 0:
            return False
    return True
while 1:
    n = int(sys.stdin.readline())
    if n == 0:
        break
    cnt = 0
    for i in range(n + 1, 2 * n + 1):
        if sosu(i):
            cnt += 1
    print(cnt)