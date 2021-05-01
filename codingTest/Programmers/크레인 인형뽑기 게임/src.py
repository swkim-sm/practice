def solution(board, moves):
    answer = 0
    n = len(board)
    stack = [0]
    for m in moves:
        for i in range(n):
            if board[i][m-1] != 0: 
                if stack[-1] == board[i][m-1]:
                    stack.pop()
                    answer += 1
                else:
                    stack.append(board[i][m-1])
                board[i][m-1] = 0
                break
    return answer*2
