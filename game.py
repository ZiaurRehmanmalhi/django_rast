def display_board(board):
    for row in board:
        for column in row:
            print(column, end=" ")
        print()


def check_win(board, player):
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] == player:
            return True
    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False


def check_draw(board):
    for row in board:
        if "." in row:
            return False
    return True

# Function to play the game


def play_game():
    board = [["." for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        display_board(board)
        print("It's", current_player, "turn.")

        row = int(input("Enter a row (1-3): ")) - 1
        col = int(input("Enter a column (1-3): ")) - 1

        if board[row][col] == ".":
            board[row][col] = current_player

            if check_win(board, current_player):
                display_board(board)
                print("Congratulations! Player", current_player, "wins!")
                break
            elif check_draw(board):
                display_board(board)
                print("It's a draw!")
                break

            current_player = 'O' if current_player == 'X' else 'X'
        else:
            print("Invalid move. Try again.")

play_game()
