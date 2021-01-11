# case 1
print(len(input().split()))

# case 2
a = input()
if len(a) == a.count(' '):
    print(0)
else:
    a = a.strip()
    print(a.count(' ') + 1)