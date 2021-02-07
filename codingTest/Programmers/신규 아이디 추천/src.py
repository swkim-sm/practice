def solution(new_id):
    answer = ''
    # step 1
    answer = new_id.lower()
    # step 2
    tmp = ''
    for i, s in enumerate(answer):
        if s.isdigit() or s.isalpha() or s in ['-', '_', '.']:
            tmp += s
    answer = tmp
    tmp = ''
    # step 3
    prev_dot = False
    for i, s in enumerate(answer):
        if s == '.' and not prev_dot:
            prev_dot = True
            tmp += s
        elif s == '.' and prev_dot:
            continue
        else:
            prev_dot = False
            tmp += s
            
    answer = tmp
    tmp = ''
    
    # step 4
    tmp = list(answer)
    if len(tmp) > 0 and tmp[0] == '.':
        del tmp[0]
    if len(tmp) > 0 and tmp[-1] == '.':
        del tmp[-1]
    answer = ''.join(tmp)
    
    # step 5 
    if not tmp:
        answer = 'a'
    
    # step 6
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:14]

    # step 7
    if len(answer) <= 2:
        answer += answer[-1]
        answer += answer[-1]
        answer = answer[:3]

    #print(answer)
    return answer
