n = int(input())
n_fact = 1
for i in range(1, n+1):
    n_fact *= i

ans = 0
while True:
    r = n_fact % 10
    if r == 0:
        ans += 1
    else:
        break
    n_fact //= 10
print(ans)

'''
more simple solution
설명 : 뒤에 0이 붙는 경우는 10(2*5)이 곱해지는 경우인데, 2는 짝수마다 들어 있고 5의 개수를 세어주면 된다
25와 125는 한 수에 5가 2개인 경우와 3개인 경우도 고려해 준 것이다.

print(n//5 + n//25 + n//125)

'''