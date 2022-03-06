import sys
I = sys.stdin.readline

def solution(N, rope):
    max_value = 0
    rope.sort() # O(nlog(n))
    for i in range(N):
        weight = (N-i)*rope[i]
        if weight > max_value:
            max_value = weight
    return max_value 

def solution_upgrade(n):
    rope = [0] * 10001
    for _ in range(n):
        rope[int(I())] += 1
    max_weight, s = 0, 0
    for tmp_weight in range(10000,-1,-1): #O(1)
        s += rope[tmp_weight]
        max_weight = max(max_weight, tmp_weight * s)
    print(max_weight)

if __name__ == "__main__":
    N = int(I())
    rope = []
    for i in range(N):
        rope.append(int(I()))
    
    answer = solution(N, rope)
    print(answer)