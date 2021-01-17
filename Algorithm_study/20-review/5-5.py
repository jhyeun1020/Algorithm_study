input()
score = [i for i in map(int, input().split())]
print(sum(i/(max(score))*100 for i in score)/len(score))