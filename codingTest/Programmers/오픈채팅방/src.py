def solution(record):
    answer = []
    user = {}
    for r in record:
        log = r.split()
        if log[0] == "Enter":
            user[log[1]] = log[2]
            answer.append("E"+log[1])
        elif log[0] == "Leave":
            answer.append("L"+log[1])
        else:
            user[log[1]] = log[2]
    n = len(answer)
    for i in range(n):
        if answer[i][0] == "E":
            answer[i] = user[answer[i][1:]] + "님이 들어왔습니다."
        else:
            answer[i] = user[answer[i][1:]] + "님이 나갔습니다."

    return answer
