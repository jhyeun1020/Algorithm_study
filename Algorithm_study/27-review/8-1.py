A, B, C = map(int,input().split())
# case 1
if B>=C:
    print(-1)
else:
    print(int(A/(C-B))+1)

# case 2
print(-1 if B>=C else int(A/(C-B))+1)