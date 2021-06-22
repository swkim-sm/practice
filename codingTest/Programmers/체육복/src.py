def solution(n, lost, reserve):
    answer = 0
    students = [1] * (n+1)
    
    # 도난당한 학생 체육복 -1
    for l in lost:
        students[l] -= 1
    # 여벌 있는 학생 체육복 +1
    for r in reserve:
        students[r] += 1
    
    
    # 체육복 개수가 2인 학생이 0인 학생에게 빌려줌
    for i in range(1, n):
        if students[i] == 0:
            # 뒷 번호가 여벌이 있는 경우
            if i > 1 and students[i-1] == 2:
                students[i] = 1
                students[i-1] = 1
            elif students[i+1] == 2:
                students[i] = 1
                students[i+1] = 1
        print(i, students)
    # 마지막 학생 처리
    if students[-1] == 0:
        if n > 1 and students[-2] == 2:
            students[-1] = 1
            students[-2] = 1
    
    # 체육복 개수가 1개 이상인 경우 세기
    print(students)
    for student in students[1:]:
        if student > 0:
            answer += 1
    return answer
