import sys
Input = sys.stdin.readline
h, w = map(int, Input().split())
heights = list(map(int, Input().split()))

left_idx = 0
answer = 0
while left_idx < w-2:
    right_idx = -1
    for i in range(heights[left_idx], 0, -1):
        for j in range(left_idx+1, w):
            if heights[j] >= i:
                if j == left_idx+1:
                    left_idx += 1
                    right_idx = 0
                    break
                right_idx = j
                break
        if right_idx != -1 or not right_idx:
            break

    if not right_idx:
        continue
    elif right_idx != -1:
        max_h = min(heights[left_idx], heights[right_idx])
        for i in range(left_idx+1, right_idx):
            answer += (max_h - heights[i])
    else:
        break
    # print(left_idx, right_idx, answer)
    left_idx = right_idx
                
print(answer)