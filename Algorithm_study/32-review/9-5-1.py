N = 123456*2
prime = N*[True]
for i in range(2,int(N**0.5)+1):
    if prime[i-1]:
        for j in range(2 * i, N + 1, i):
            prime[j - 1] = False
def prime_check(a):
    cnt = 0
    for i in range(a+1,2*a+1):
        if prime[i-1]:
            cnt += 1
    print(cnt)
while True:
    a = int(input())
    if a == 0:
        break
    prime_check(a)