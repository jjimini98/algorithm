import sys

print("=====================================")
lis = []
for x in range(int(sys.stdin.readline())):
    lis.append(int(sys.stdin.readline()))
    lis = sorted(lis)
    print(lis[x])
