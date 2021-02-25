N = int(input())
agna = [list(input().split()) for i in range(N)]
agna.sort(key = lambda x: int(x[0]))
for i in range(N):
    print(agna[i][0],agna[i][1])