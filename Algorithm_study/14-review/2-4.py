x = int(input())
y = int(input())
# case 1
if x>0:
    if y>0:
        print(1)
    else:
        print(4)
else:
    if y>0:
        print(2)
    else:
        print(3)
# case 2
if x>0:
    print(1 if y>0 else 4)
else:
    print(2 if y>0 else 3)