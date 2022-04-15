import sys
input = sys.stdin.readline
n, m = map(int, input().split())
names = {}

for i in range(1, n+1):
    name = input().rstrip()
    names[name] = i
    names[str(i)] = name

for i in range(m):
    q = input().rstrip()
    print(names[q])