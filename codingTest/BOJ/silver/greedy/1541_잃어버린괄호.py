import sys

def solution(formula):
    min_value = 0
    formula = formula.split('-')
    sub_formula = []

    for f in formula:
        sub_formula.append(sum(map(int, f.split('+'))))

    min_value = sub_formula[0] - sum(sub_formula[1:])
    return min_value

if __name__=="__main__":
    I = sys.stdin.readline()
    answer = solution(I)
    print(answer)
