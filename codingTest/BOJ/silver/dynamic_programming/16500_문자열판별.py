import sys
Input = sys.stdin.readline

S = Input().rstrip()
N = int(Input())
A = []
for _ in range(N):
    A.append(Input().rstrip())

pos = len(S)
poses = [pos]
pos -= 1

for i in range(pos, -1, -1):
    for j in poses:
        if S[i:j] in A:
            poses.append(i)
            break

if not poses[-1] :
    print(1)
else:
    print(0)

    
