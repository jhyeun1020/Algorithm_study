# case 2
def factorial(N,result):
    if N <= 1:
        print(result)
        return
    factorial(N-1,N*result)
factorial(int(input()), 1)