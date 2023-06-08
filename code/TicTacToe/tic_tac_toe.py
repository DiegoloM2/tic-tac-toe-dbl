def display_board(board):
    """
    Displays the Tic-Tac-Toe board.

    Args:
        board (list): List representing the Tic-Tac-Toe board.
    """

    board_display = ""

    for i in range(0, 9):
        if (i > 0 and i % 3 == 0):
            board_display += "\n"
        if (board[i] == 0):
            board_display += "- "
        if (board[i] == 1):
            board_display += "O "
        if (board[i] == -1):
            board_display += "X "
    board_display += "\n\n"
    print(board_display)
    return board_display



def player_turn(board, user:int):
    """
    Performs a turn for a User (X) by updating the board.

    Args:
        board (list): List representing the Tic-Tac-Toe board.
        user: 1 for "O", -1 for "X"

    Returns:
        bool: True if the turn was successful, False otherwise.
    """
    userString = "O" if user == 1 else "X"
    pos = input(f"Enter {userString} position from [1...9]: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Space occupied, try again.")
        player_turn(board, user)
    board[pos - 1] = user
    return True



def minimax(board, player):
    """
    Finds the optimal move for the Tic-Tac-Toe game using the minimax algorithm.

    Args:
        board (list): List representing the Tic-Tac-Toe board.
        player (int): Current player (-1 for X, 1 for O).

    Returns:
        int: The optimal value of the move for the current player.
    """
    # Check if the game has ended
    score = analyze_board(board)
    if score != 0:
        return score * player  # Return the score (win/loss/draw) for the current player

    optimal_move = -1  # Position of the optimal move
    best_value = -2  # Initial value for comparison

    for i in range(0, 9):
        if board[i] == 0:  # Check if the position is available
            board[i] = player  # Make the move for the current player

            # Recursively evaluate the opponent's moves
            opponent_value = -minimax(board, player * -1)

            if opponent_value > best_value:
                best_value = opponent_value
                optimal_move = i

            board[i] = 0  # Undo the move for backtracking

    if optimal_move == -1:
        return 0  # If no available move, return 0 (draw)

    return best_value  # Return the optimal value for the current player    
    
def CompTurn(board):
    pos=-1;
    value=-2;
    for i in range(0,9):
        if(board[i]==0):
            board[i]=1;
            score=-minimax(board, -1);
            board[i]=0;
            if(score>value):
                value=score;
                pos=i;
    board[pos]=1;


def analyze_board(board):
    """
    Analyzes the Tic-Tac-Toe board and checks for a win or draw.

    Args:
        board (list): List representing the Tic-Tac-Toe board.

    Returns:
        int: Result of the game (-1 for X win, 1 for O win, 0 for draw).
    """
    # List of winning combinations
    cb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]

    for i in range(0, 8):
        # Check if any winning combination is present
        if (
            board[cb[i][0]] != 0 and
            board[cb[i][0]] == board[cb[i][1]] and
            board[cb[i][0]] == board[cb[i][2]]
        ):
            return board[cb[i][2]]  # Return the winning player (-1 or 1)

    return 0  # No winning combination, return 0 for a draw


def main():
    # Get user's choice for single player or multiplayer
    choice = input("Enter 1 for single player, 2 for multiplayer: ")
    choice = int(choice)

    # Initialize the game board
    board = [0, 0, 0, 0, 0, 0, 0, 0, 0]

    if choice == 1:
        print("Computer : O Vs. You : X")
        player = input("Enter to play 1(st) or 2(nd) :")
        player = int(player)

        for i in range(0, 9):
            if analyze_board(board) != 0:
                break

            if (i + player) % 2 == 0:
                CompTurn(board)
            else:
                display_board(board)
                player_turn(board, 1)  # Player's turn

    else:
        for i in range(0, 9):
            if analyze_board(board) != 0:
                break

            if i % 2 == 0:
                display_board(board)
                player_turn(board, 1)  # Player 1's turn
            else:
                display_board(board)
                player_turn(board, -1)  # Player 2's turn

    x = analyze_board(board)
    if x == 0:
        display_board(board)
        print("Draw!!!")
    if x == -1:
        display_board(board)
        print("X Wins!!! Y Loose !!!")
    if x == 1:
        display_board(board)
        print("X Loose!!! O Wins !!!!")

       