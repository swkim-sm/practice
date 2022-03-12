import sys
from collections import defaultdict
from unicodedata import digit
Input = sys.stdin.readline

n = int(Input())
words = []
alphabet_priority = defaultdict(int)

for _ in range(n):
    alphabet = Input().rstrip()
    words.append(alphabet)
    for i in range(len(alphabet)):
        alphabet_priority[alphabet[i]] += 10**(len(alphabet)-i)

alphabets = list(alphabet_priority)
alphabets.sort(key=lambda x:alphabet_priority[x])
base_n = 10 - len(alphabets)
for a in alphabets:
    alphabet_priority[a] = base_n
    base_n += 1

answer = 0
for word in words:
    m = len(word)
    for i in range(m):
        answer += (10**(m-i-1))*alphabet_priority[word[i]]
print(answer)