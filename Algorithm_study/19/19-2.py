import sys
M, N = map(int, sys.stdin.readline().split())
def prime(i):
    if i == 1:
        return False
    else:
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                return False
        return True
for i in range(M, N+1):
    if prime(i):
        print(i)