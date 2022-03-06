import sys

def solution(N):
    big_bag = (N-1) // 5 + 1
    small_bag = 0

    while big_bag >= 0:
        tmp_weight = 5*big_bag + 3*small_bag
        
        if tmp_weight == N:
            return big_bag+small_bag
        
        big_bag -= 1
        small_bag = (N - 5*big_bag - 1) // 3 + 1
    return -1

def solution_upgrade(sugar):
    bag = 0
    while sugar >= 0 :
        if sugar % 5 == 0 : 
            bag += (sugar // 5)
            return bag
        sugar -= 3  
        bag += 1 
    return -1

if __name__ == "__main__":
    N = int(sys.stdin.readline())
    answer = solution_upgrade(N)
    print(answer)
