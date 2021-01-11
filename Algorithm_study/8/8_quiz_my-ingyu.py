a = int(input())

llist = []
for _ in range(a):
    i = input()
    long = 0; score =0
    for j in range(len(i)):
        if i[j] == 'O':
            long += 1
        else:
            score = score + long * long
            long = 0
        llist.append(score)

average = sum(llist)/a
people = 0

print(average)
for i in llist:
    if average < i:
        people += 1
print("%0.2f%%"%float(people/a*100))