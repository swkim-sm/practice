import sys

Input = sys.stdin.readline
n = int(Input())
max_weights = list(map(int, Input().split()))
m = int(Input())
boxes = list(map(int, Input().split()))

max_weights.sort(reverse=True)
boxes.sort(reverse=True)

answer = 0
if max_weights[0] < boxes[0]:
    answer = -1
else:
    while boxes:
        for weight in max_weights:
            for box in boxes:
                if weight >= box:
                    boxes.remove(box)
                    break
        answer += 1
print(answer)