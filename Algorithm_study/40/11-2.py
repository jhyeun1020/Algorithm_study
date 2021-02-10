llist = {}
for i in range(1,1000001):
    stack = i
    i = str(i)
    for j in range(len(i)):
        stack += int(i[j])
    llist[int(i)] = stack
a = int(input())
for key,value in llist.items():
    if value == a:
        print(key)
        break
else:
    print(0)
# break 문에 걸려서 for 문을 빠져나온 게 아니라면 else 문 실행