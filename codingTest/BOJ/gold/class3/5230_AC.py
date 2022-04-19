import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    p = input().rstrip()
    n = int(input())
    arr = deque(input().rstrip()[1:-1].split(','))
    if n == 0:
        arr = []
    # print(arr)
    error_flag = False
    reverse_flag = False
    for c in p:
        if len(arr) > 0:
            if c == 'R':
                if reverse_flag:
                    reverse_flag = False
                else:
                    reverse_flag = True
            else:
                if reverse_flag:
                    arr.pop()
                else:
                    arr.popleft()

        elif c == 'D':
            error_flag = True
            break

    if error_flag:
        print("error")
    else:
        if reverse_flag:
            arr.reverse()
        if arr:
            print('['+','.join(arr)+']')
        else:
            print('[]')