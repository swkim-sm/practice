import sys

Input = sys.stdin.readline

def solution(n, dice):
    if n == 1:
        tmp = sorted(dice)
        return sum(dice) - tmp[-1]

    sumLists = []
    sumLists.append(min(dice[0],dice[5]))
    sumLists.append(min(dice[1],dice[4]))
    sumLists.append(min(dice[2],dice[3]))
    sumLists = sorted(sumLists)

    one_side = sumLists[0]
    two_side = sum(sumLists[:2])
    three_side = sum(sumLists)

    min_sum = 4*(n-2)*two_side + 4*(n-1)*two_side + 4*three_side + (n-2)*(5*n-6)*one_side

    
    # three_side = [dice[0]+dice[1]+dice[2], dice[0]+dice[1]+dice[3],
    #               dice[0]+dice[2]+dice[4], dice[0]+dice[3]+dice[4],
    #               dice[1]+dice[2]+dice[5], dice[1]+dice[3]+dice[5],
    #               dice[1]+dice[4]+dice[5], dice[3]+dice[4]+dice[5]] 
    # two_side = [dice[0]+dice[1], dice[0]+dice[2], dice[0]+dice[3],
    #             dice[0]+dice[4], dice[1]+dice[2], dice[1]+dice[3],
    #             dice[1]+dice[5], dice[2]+dice[4], dice[2]+dice[5],
    #             dice[3]+dice[4], dice[3]+dice[5], dice[4]+dice[5]]
    
    # three_side.sort()
    # two_side.sort()
    # dice.sort()


    # min_sum = 4*(n-2)*two_side[0] + 4*(n-1)*two_side[0] + 4*three_side[0] + (n-2)*(5*n-6)*dice[0]
    return min_sum

if __name__=="__main__":
    N = int(Input())
    dice = list(map(int, Input().split()))
    print(solution(N, dice))
    