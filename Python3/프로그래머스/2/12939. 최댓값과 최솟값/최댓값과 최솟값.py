def solution(s):
    answer = f'{min(map(int, s.split()))} {max(map(int, s.split()))}'
    return answer