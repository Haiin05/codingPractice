def solution(board, moves):
    answer = 0

    column = []
    i = 0
    while i < len(board) :
        j = 0
        a = []
        while j < len(board) :
            x = board[j][i]
            if x != 0 :
                a.append(x)
                j += 1
            else :
                j += 1
        column.append(a)
        i += 1

    icon_bucket = []
    for n in range(len(moves)) :
        col_num = moves[n] - 1
        if column[col_num] != [] :
            icon = column[col_num][0] 

            if icon_bucket != [] :
                if icon == icon_bucket[-1] : 
                    icon_bucket.pop(-1) # remove(icon)으로 했을때 답이 안나오는 경우도 있었음
                    column[col_num].pop(0)
                    answer += 2
                else :
                    icon_bucket.append(icon)
                    column[col_num].pop(0)  
            else :
                icon_bucket.append(icon)
                column[col_num].pop(0)
        else :
            pass
    print(answer)
    
solution(board, moves)