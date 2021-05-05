from itertools import combinations, permutations

def is_faulty(user, banned):
    n = len(user)
    if n != len(banned):
        return False

    for i in range(n):
        if banned[i] != "*" and user[i] != banned[i]:
            return False
    return True

def solution(user_id, banned_id):
    answer = 0
    n = len(banned_id)

    # user_id 간의 순열 조합
    user_candi = list(combinations(user_id, n))
    banned_candi = list(permutations(banned_id, n))
    # 순열 조합이 banned_id 와 같은지 비교
    answers = set()
    for user in user_candi:
        for banned in banned_candi:
            flag = True
            for i in range(n):
                if not is_faulty(user[i], banned[i]):
                    flag = False
                    break

            if flag : 
                answers.add(user)
    answer = len(answers)
    return answer
