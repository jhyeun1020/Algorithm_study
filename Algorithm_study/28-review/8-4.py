# case 1
A, B, V = map(int, input().split())
print(int((V-A)/(A-B)+1.999999))
# case 2
import math
A, B, V = map(int, input().split())
print(math.ceil((V-A)/(A-B)+1))

# 엄밀히 따지면 case 1은 틀렸다 소수점 6자리수를 넘어가게 되면 값이 달라지기 때문