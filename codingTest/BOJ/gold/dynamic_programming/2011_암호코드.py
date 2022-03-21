import sys
code = [0]+list(map(int, list(sys.stdin.readline().rstrip())))

len_of_code = len(code)
dp = [1 for _ in range(len_of_code+1)]
flag = False

for i in range(1, len_of_code):
    if code[i] == 0:
        if 0 < code[i-1] < 3:
            dp[i+1] = dp[i-1]
        else:
            flag = True
            break
    else:
        dp[i+1] = dp[i]
        if code[i-1] == 1 or (code[i-1] == 2 and 0 < code[i] < 7):
            dp[i+1] += dp[i-1]
    dp[i+1] %= 1000000
    # print(code[i], i, dp[i+1])

if flag:
    print(0)
else:
    print(dp[-1])
    