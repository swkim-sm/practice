import sys

Input = sys.stdin.readline

def get_num_of_days(mm, dd):
    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]
    num_of_days = dd
    for m in range(mm):
        num_of_days += days_in_month[m]
    return num_of_days

def get_days_array(dates):
    days_in_num = []
    for date in dates:
        start_day = get_num_of_days(date[0], date[1])
        end_day = get_num_of_days(date[2], date[3])

        days_in_num.append((start_day, end_day))
    return days_in_num

def solution(n, dates):
    # must include day
    must_include = (get_num_of_days(3, 1), get_num_of_days(11, 30)) # 60, 334

    cnt = 0 # num of flowers
    end = 0 # the day the last flower fall
    target = must_include[0] # end of flower

    while dates:
        # break condition
        if must_include[1] < target or target < dates[0][0]:
            break

        # find the last flower to fall
        for _ in range(len(dates)):
            if target >= dates[0][0]:
                # update last day
                if end <= dates[0][1]:
                    end = dates[0][1]
                dates.remove(dates[0])
            else:
                break
        target = end
        cnt += 1         

    if target <= must_include[1]:
        return 0
    return cnt
       

if __name__ == "__main__":
    N = int(Input())
    dates = []
    for _ in range(N):
        dates.append(list(map(int, Input().split())))
    
    flower_days = get_days_array(dates)
    flower_days.sort(key=lambda x:(x[0], x[1]))
    print(solution(N, flower_days))