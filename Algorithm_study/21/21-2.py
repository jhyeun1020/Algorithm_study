# 백준 통못
import sys
def sosu(n):
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
for _ in range(int(sys.stdin.readline())):
    n = int(sys.stdin.readline())
    for i in range(2,n//2+1):
        if sosu(i):
            if sosu(n-i):
                a = [i,n-i]
    print(a[0],a[1])