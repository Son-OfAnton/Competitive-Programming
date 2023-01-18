# https://codeforces.com/gym/421441/problem/C

board_num = int(input())

for _ in range(board_num):
    input()
    board = []
    for i in range(8):
        board.append(input())
    
    bishop_found = False
    
    for rx in range(1,7):
        for cx in range(1,7):
            if board[rx][cx] == '#' and board[rx-1][cx-1] == '#' \
                and board[rx-1][cx+1] == '#' and board[rx+1][cx-1] == '#' \
                and board[rx+1][cx+1] == '#':

                print(rx+1, cx+1)
                bishop_found = True
                break
        
        if bishop_found:
            break
