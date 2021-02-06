# 이거는 복습이 필요합니다
def fibo(n):
    if n <= 1:
        return n
    return fibo(n-1)+fibo(n-2)
print(fibo(int(input())))