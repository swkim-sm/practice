import sys
from collections import deque

Input = sys.stdin.readline

def solution(A, B):
    dq = deque([(A, 1)])
    # visited = [A]
    while dq:
        cur, n = dq.popleft()

        if cur == B:
            return n
        
        elem_1 = cur*2
        elem_2 = int(str(cur)+'1')

        if elem_1 <= B:
            dq.append((elem_1, n+1))
            # visited.append(elem_1)
        if elem_2 <= B:
            dq.append((elem_2, n+1))
            # visited.append(elem_2)

    return -1
if __name__ == "__main__":
    A, B = map(int, Input().split())
    answer = solution(A, B)
    print(answer)