t = int(input())
for _ in range(t):
    k = int(input())
    n = int(input())
    # first floor
    dp = []
    dp.append([i+1 for i in range(n)])
    for i in range(k):
        cur_arr = []
        cur_n = 0
        for j in range(n):
            cur_n += dp[-1][j]
            cur_arr.append(cur_n)
        dp.append(cur_arr)
    print(dp[-1][-1])