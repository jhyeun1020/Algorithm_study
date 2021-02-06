def factory(N):
    if N == 0:
        return 1
    return factory(N-1)*N
print(factory(int(input())))