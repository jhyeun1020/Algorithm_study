# case 1
import sys
llist = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
llist.sort()
print('\n'.join(map(str, llist)))

# case 2
llist = [int(sys.stdin.readline()) for _ in range(int(sys.stdin.readline()))]
for i in sorted(llist):
    print(i)