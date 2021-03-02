N = int(input())
square = [[0 for _ in range(N)] for _ in range(N)]
def star(x):
    global square
    if x == 3:
        square[0][:3] = square[2][:3] = [1]*3
        square[1][:3] = [1,0,1]
        return
star(N)
for i in square:
    for j in i:
        if j:
            print('*', end='')
        else:
            print(' ', end='')
    print()
# 다시 다시 다시 다시 다시 다시 다시 다시 다시 다시