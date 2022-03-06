# input
N = int(input())
amounts = []
for i in range(N):
    amounts.append(int(input()))

# perform
memory = [0, 0, 0]
current = [0, 0, 0]
for amount in amounts:
    current[0] = memory[2] + amount
    current[1] = memory[0] + amount
    current[2] = max(memory)
    memory = current[:]

# output
print(max(current))