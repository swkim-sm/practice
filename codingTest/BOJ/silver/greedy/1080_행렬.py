import sys

I = sys.stdin.readline

def solution(N, M, board, target):
    cnt = 0
    for i in range(N-2):
        for j in range(M-2):
            if board[i][j] != target[i][j]:
                cnt += 1
                for x in range(3):
                    for y in range(3):
                        board[i+x][j+y] = abs(board[i+x][j+y]-1)

    if board == target:
        return cnt
    else:
        return -1
                


if __name__ == "__main__":
    N, M = map(int, I().split())
    b1 = []
    b2 = []
    for _ in range(N):
        b1.append(list(map(int, list(I())[:M])))
    for _ in range(N):
        b2.append(list(map(int, list(I())[:M])))

    
    print(solution(N, M, b1, b2))
