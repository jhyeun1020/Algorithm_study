# case 1
A = int(input())
B = int(input())
C = []
C.append(A*(B%100%10))
C.append(A*(B%100//10))
C.append(A*(B//100))
print(C[0],C[1],C[2],C[0]+C[1]*10+C[2]*100,sep='\n')

# case 2
print(A*(B%100%10),A*(B%100//10),A*(B//100),A*B,sep='\n')