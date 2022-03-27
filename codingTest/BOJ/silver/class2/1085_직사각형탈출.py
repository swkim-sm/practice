x, y, w, h = map(int, input().split())
answer = min(x, w-x, y, h-y)
print(answer)