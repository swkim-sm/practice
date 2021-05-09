import math

def solution(w,h):
    answer = w*h
    w_unit = w/h
    # 한 주기 계산
    pre_floor = 0.0
    i = 0
    unit_sum = 0
    while True:
        i += 1
        cur_ceil = math.ceil(i*w_unit)
        unit_sum += (cur_ceil - pre_floor)
        pre_floor = math.floor(i*w_unit)
        if cur_ceil == pre_floor:
            break
    # print(unit_sum, i)
    answer -= unit_sum * (h/i)
    return answer
