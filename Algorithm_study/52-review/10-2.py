def fibo(N):
    if N <= 1:
        return N
    return fibo(N-1)+fibo(N-2)
print(fibo(int(input())))