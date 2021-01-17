for i in range(int(input())):
    a = input()
    score = 0
    stack = 0
    for i in a:
        if i == 'O':
            score += 1+stack
            stack += 1
        else:
            stack = 0
    print(score)