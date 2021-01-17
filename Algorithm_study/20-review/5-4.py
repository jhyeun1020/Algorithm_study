# case 1
num = [int(input()) for i in range(10)]
dev = []
for i in num:
    if i%42 not in dev:
        dev.append(i%42)
print(len(dev))

# 집합 사용
num = [int(input())%42 for i in range(10)]
print(len(set(num)))