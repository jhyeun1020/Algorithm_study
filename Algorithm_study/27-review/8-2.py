# case 1
a = int(input())
if a == 1:
    print(1)
else:
    stack = 0
    while 1:
        stack += 1
        if 3*stack*(stack-1)+2 <= a < 2+3*(stack+1)*stack:
            print(stack+1)
            break

# case 2
stack = 0
a = int(input())
while a>=3*stack*(stack+1)+2:
    stack+=1
print(stack+1)