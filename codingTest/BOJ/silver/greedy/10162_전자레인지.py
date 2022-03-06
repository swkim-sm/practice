import sys
I = sys.stdin.readline

def solution(time):
    if time % 10 :
        return -1
    A, B, C = 0, 0, 0
    # 5 min == 300 sec
    A = str(time // 300)
    time %= 300
    # 1 min == 60 sec
    B = str(time // 60)
    time %= 60
    # 10 sec
    C = str(time // 10)
    return ' '.join([A, B, C])
if __name__ == "__main__":
    T = int(I())
    answer = solution(T)
    print(answer)