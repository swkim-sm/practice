def solution(skill, skill_trees):
    answer = 0
    for st in skill_trees:
        tmp = []
        for s in st:
            if s in skill:
                tmp.append(s)
        sz = len(tmp)

        if skill[:sz] == ''.join(tmp):
            answer += 1

    return answer
