    
def solution(numbers, target):
    answer = 0
    
    def dfs(idx, value):
        answer = 0
        if idx == len(numbers):
            if value == target:
                return 1
            else:
                return 0
        else:
            x = numbers[idx]
            idx += 1
            answer += dfs(idx, value+x)
            answer += dfs(idx, value-x)

            return answer
    answer += dfs(1, numbers[0])
    answer += dfs(1, -numbers[0])
    
    return answer
