count = 0
store = ''
aa = []
a = int(input())
for _ in range(a):
    for i in input():
        if i != store and i in aa:
            count += 1
            break
        aa.append(i)
        store = i
    aa.clear()
print(a-count)