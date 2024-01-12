def solution(board, h, w):
    answer = 0
    size = len(board)
    check = [(0,-1),(0,1),(-1,0),(1,0)]
    for i in check:
        h_check = h + i[0]
        w_check = w + i[1]
        if (0 <= h_check < size) and (0 <= w_check < size):
            if board[h][w] == board[h_check][w_check]:
                answer += 1
    return answer