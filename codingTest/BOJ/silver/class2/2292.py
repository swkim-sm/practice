n = int(input())
i, pre = 0, 1
while True:
    cur = pre + i*6
    if pre <= n <= cur:
        break
    pre = cur
    i += 1
print(i+1)