def get_gcd(x, y):
    if x < y:
        (x, y) = (y, x)
    while y!=0:
        (x, y) = (y, x%y)
    return x

def solution(w,h):
    answer = w*h
    gcd = get_gcd(w, h)
    unit = (w+h) / gcd - 1
    answer -= unit * gcd
    return answer
