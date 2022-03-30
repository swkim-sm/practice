n = input()
alpha = {'0':0, '1':1, '2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'A':10, 'B':11, 'C':12, 'D':13, 'E':14 , 'F':15}
answer = 0
for i in range(len(n)):
    answer += (alpha[n[i]]*16**(len(n)-i-1))
print(answer)