import sys
Input = sys.stdin.readline

N, M = map(int, Input().split())

know_truth = list(map(int, Input().split()))
num_of_knowing_truth = know_truth[0]
know_truth.pop(0)

participant = []
for _ in range(M):
    participant.append(list(map(int, Input().split()))[1:])

while know_truth:
    cur = know_truth.pop()
    for p in participant:
        if cur in p:
            know_truth.extend(p)
            participant.remove(p)
            break

print(len(participant))

