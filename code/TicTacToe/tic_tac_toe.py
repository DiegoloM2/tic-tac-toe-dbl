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
        position to be played now
    """
    userString = "O" if user == 1 else "X"
    pos = input(f"Enter {userString} position from [1...9]: ")
    pos = int(pos)
    if board[pos - 1] != 0:
        print("Space occupied, try again.")
        player_turn(board, user)
    board[pos - 1] = user
    return board, pos



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
    """
    Function to determine and make the computer's optimal turn in a Tic-Tac-Toe game.

    Parameters:
    - board: List representing the current state of the Tic-Tac-Toe board.

    Returns:
    - None

    Side Effects:
    - Modifies the board list to make the optimal move for the computer (uses value 1).

    Algorithm:
    1. Initialize the position (pos) variable for the optimal move to -1.
    2. Initialize the initial value (value) for the best score to -2.
    3. Iterate over the board positions from 0 to 8.
        a. Check if the board position is empty (board[i] == 0).
        b. If it is empty, assume the current position for the computer's move by setting it to 1.
        c. Calculate the opponent's best score by recursively calling the minimax function with the updated board and player as -1.
        d. Reset the current position on the board by setting it back to 0.
        e. Compare the score obtained with the current best value.
        f. If the score is higher, update the best value and the optimal position.
    4. Set the board at the optimal position to 1, representing the computer's move.
    """
    pos = -1  # Initialize the position variable for the optimal move
    value = -2  # Initialize the initial value for the best score

    for i in range(0, 9):
        if board[i] == 0:  # If the board position is empty
            board[i] = 1  # Assume the current position for the computer's move
            score = -minimax(board, -1)  # Recursively calculate the opponent's best score
            board[i] = 0  # Reset the current position on the board

            if score > value:  # Compare the score obtained with the current best value
                value = score  # Update the best value
                pos = i  # Update the optimal position

    board[pos] = 1  # Set the board at the optimal position to 1, representing the computer's move
    return board, pos

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
                player_turn(board, -1)  # Player's turn

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

def chooseGame():
    choice = input("Enter 1 for single player, 2 for multiplayer: ")
    if int(choice) == 1:
        print("Great, you will play against an Artificial Intelligence")
        return int(choice)
    elif int(choice) == 2:
        print("Great, you will play multiplayer")
        return int(choice)

    else: chooseGame()
