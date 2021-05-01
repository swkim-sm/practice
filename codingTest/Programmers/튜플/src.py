def solution(s):
    answer = []

    # transform s to list
    i = 1
    s_list = []
    while i < len(s):
        if s[i] == "{":
            j = i+1
            tmp_s = ""
            while s[j] != "}":
                tmp_s += s[j]
                j += 1
            s_list.append(set(map(int, tmp_s.split(","))))
        i += 1
    # sort by len
    s_list = sorted(s_list, key=len)

    # 작은 것부터 추가되는 숫자 찾기
    num = len(s_list)
    answer.append(list(s_list[0])[0])
    print(answer)
    for n in range(num-1):
        answer.extend(list(s_list[n+1]-s_list[n]))
    return answer
