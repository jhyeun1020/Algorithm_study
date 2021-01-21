alphabet = input().upper()
a = []
for i in range(65,91):
    a.append(alphabet.count(chr(i)))
if a.count(max(a))>1:
    print('?')
else:
    print(chr(a.index(max(a))+65))