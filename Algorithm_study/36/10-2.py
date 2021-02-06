pibo = [0,1,1]
for i in range(int(input())):
    pibo[2] = pibo[0]+pibo[1]
    pibo[0] = pibo[1]
    pibo[1] = pibo[2]
print(pibo[0])