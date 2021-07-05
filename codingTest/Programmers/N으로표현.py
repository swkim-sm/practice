def solution(N, number):
    answer = -1
    arr = [{N}]
    print(arr)
    if N == number:
        return 1
    for n in range(1, 8):
        tmp_set = {int(str(N)*(n+1))}
        for half in range(0, n//2+1):
            for i in arr[half]:
                for j in arr[n-1-half]:
                    tmp_set.add(i+j)
                    tmp_set.add(i*j)
                    tmp_set.add(i-j)
                    tmp_set.add(j-i)
                    if i != 0 : tmp_set.add(j//i)
                    if j != 0 : tmp_set.add(i//j)
        if number in tmp_set:
            return n+1
        arr.append(tmp_set)
    return answer
