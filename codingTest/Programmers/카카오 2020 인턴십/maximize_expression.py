from itertools import permutations 

def calc(n1, n2, op):
    if op == '+':
        return n1 + n2
    elif op == '-':
        return n1 - n2
    else:
        return n1 * n2
    
def solution(expression):
    answer = 0
    
    # priority list of operators
    operators = ['+', '-', '*']
    priority = list(map(''.join, permutations(operators)))
    
    # split expression by operator
    ori_nums, ori_ops = [], []
    pre_idx = 0
    for i, v in enumerate(expression):
        if v in operators:
            ori_ops.append(v)
            ori_nums.append(int(expression[pre_idx:i]))
            pre_idx = i+1
    ori_nums.append(int(expression[pre_idx:]))
    
    # main func - calculate the result
    for p in priority:
        nums = ori_nums.copy()
        ops = ori_ops.copy()
        for i in range(3):
            cur_op = p[i]
            cur_idx = 0
            while cur_idx < len(ops):
                if cur_op == ops[cur_idx]:
                    nums[cur_idx] = calc(nums[cur_idx], nums[cur_idx+1], cur_op)
                    ops.pop(cur_idx)
                    nums.pop(cur_idx+1)
                    cur_idx -= 1
                cur_idx += 1
        
        answer = max(abs(nums[0]), answer)
    return answer
