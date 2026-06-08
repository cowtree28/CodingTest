def solution(msg):
    answer = []
    di = {}
    msg_len = len(msg)
    di_max_word_len = 1
    di_len = 26
    for i in range(1, di_len + 1):
        di[chr(64 + i)] = i
    i = 0
    while len(msg) > i:
        # 해당글자 + 뒷글자중 가장 큰 조합 찾아 answer에 append
        # print(msg[i])
        j = i+di_max_word_len
        while j > i:# 4 + 3, 4, -1
            if j > msg_len:
                j = msg_len
            if msg[i:j] in di:
                pass_len = j-i
                answer.append(di[msg[i:j]])
                break
            j -= 1
        # print(answer)
        # 해당글자부터 뒷글자까지 사전에 더함
        idx = i
        app = msg[idx]
        while idx < msg_len - 1 and app in di:
            app += msg[idx + 1]
            idx += 1
        di_len += 1
        di[app] = di_len
        if len(app) > di_max_word_len:
            di_max_word_len = len(app)
        # print(app, di_len)
        # print(pass_len)
        i += pass_len
    return answer