# func returns True when right hand is closer than left hand
def get_closer(left, right, hand, target):
    # keypad list, * = -1, # = -2
    keypad = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [-1, 0, -2]]
    # target position (x, y)
    flag = False
    target_pos = [-1, -1]
    left_pos = [-1, -1]
    right_pos = [-1, -1]
    for i in range(4):
        for j in range(3):
            if keypad[i][j] == target:
                target_pos = [i, j]
            if keypad[i][j] == left:
                left_pos = [i, j]
            if keypad[i][j] == right:
                right_pos = [i, j]

    # distance from left hand position to target
    left_dist = abs(target_pos[0]-left_pos[0]) + abs(target_pos[1]-left_pos[1])
    # distance from right hand position to target
    right_dist = abs(target_pos[0]-right_pos[0]) + abs(target_pos[1]-right_pos[1])

    # compare two distances
    if left_dist < right_dist or (left_dist == right_dist and hand == "left"):
        return False

    return True
def solution(numbers, hand):
    answer = ''

    left_pos = -1 # 왼손 위치
    right_pos = -2 # 오른손 위치

    for n in numbers:
        if n in [1, 4, 7]:
            answer += 'L'
            left_pos = n
        elif n in [3, 6, 9]:
            answer += 'R'
            right_pos = n
        else:
            closer_hand = get_closer(left_pos, right_pos, hand, n)
            if closer_hand:
                answer += 'R'
                right_pos = n
            else:
                answer += 'L'
                left_pos = n
    return answer
