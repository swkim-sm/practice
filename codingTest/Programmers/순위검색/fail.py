def solution(info, query):
    answer = []
    # info to list
    info_list = []
    for i in info:
        tmp_i = list(i.split())
        tmp_i[4] = int(tmp_i[4])
        info_list.append(tmp_i)

    # query to list
    query_list = []
    for q in query:
        tmp_q = list(''.join(q.split('and')).split())
        if tmp_q != '-':
            tmp_q[4] = int(tmp_q[4])
        query_list.append(tmp_q)
    print(query_list)
    # find info which satisfies query
    for ql in query_list:
        cnt = 0
        for il in info_list:
            if ql[4] == '-' or ql[4] <= il[4]:
                flag = True
                for i in range(4):
                    if ql[i] == '-' or ql[i] == il[i]:
                        continue
                    else:
                        flag = False
                        break
                if flag:
                    cnt += 1
            
        answer.append(cnt)
                    
    return answer
