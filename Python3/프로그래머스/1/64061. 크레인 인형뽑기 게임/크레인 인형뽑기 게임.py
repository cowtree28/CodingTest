def solution(board, moves):
    answer = 0
    n = len(board[0])
    basket = []
    
    top = [n for x in range(n)]
    # top 구하기
    for i in range(n):
        for j in range(n):
            if board[j][i] != 0:
                top[i] = j
                break
    
    
    for i in moves:
        # print(top)
        # print(top[i-1], i-1)
        if(top[i-1] >= n):
            continue
        basket.append(board[top[i-1]][i-1])
        # print(top[i-1],n)
        
        
        j = 0
        is_pop = True
        while(is_pop):
            # print(basket)
            is_pop = False
            for j in range(len(basket)-1):
                if(basket[j] == basket[j+1]):
                    basket.pop(j+1)
                    basket.pop(j)
                    answer += 2
                    is_pop = True
                    break

        top[i-1] += 1
        
        
    return answer

