a = int(input())
floor = 0
stack = 1
while a >= stack:
    floor += 1
    stack += floor
if floor%2 == 0:
    print("{}/{}".format(a-stack+floor+1,floor+1-a+stack-floor-1))
else:
    print("{}/{}".format(floor+1-a+stack-floor-1,a-stack+floor+1))