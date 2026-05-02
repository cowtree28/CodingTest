def solution(s):
    answer = ' '.join(list(map(lambda x: x[0].upper() + x[1:].lower() if len(x) > 0 else x, s.split(' '))))
    return answer