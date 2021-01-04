a = int(input())
for i in range(a):
    test = input()
    score = 0 ; total_score = 0 ; score_rase = 0
    for j in range(len(test)):
        if test[j] == 'O':
            score = 1+score_rase
            total_score += score
            score_rase += 1
        else:
            score = 0 ; score_rase = 0
    print(total_score)