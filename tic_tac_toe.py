board = [[" " for _ in range(3)] for _ in range(3)]
def print_board(board):
    for row in board:
        print('|'.join(row))
        print('-'*5)

def make_move(board, row, col, symbol):
    if board[row][col] == " ":
        board[row][col] = symbol
    else:
        print("Thaat spot is already taken!")

def is_winner(board, symbol):
    for row in board:
        if all(cell == symbol for cell in row):
            return True
        
    for col in range(3):
        if all(board[row][col] == symbol for row in range(3)):
            return True
    
    if all(board[i][i] == symbol for i in range(3)):
        return True
    
    if all(board[i][2 - i] == symbol for i in range(3)):
        return True
    
    return False
    
def is_draw(board):
    for row in board:
        if ' ' in row:
            return False
    return True
    

current_player = 'X'

while True:
    print_board(board)
    print(f"Player {current_player}'s turn.")
    
    row = int(input("Enter row (0-2): "))
    col = int(input("Enter col (0-2): "))
    make_move(board, row, col, current_player)
    if is_winner(board, current_player):
        print_board(board)
        print(f"🎉 Player {current_player} wins!")
        break
    if is_draw(board):
        print("It's a draw! 🤝")
        break
    current_player = 'O' if current_player == 'X' else 'X'
